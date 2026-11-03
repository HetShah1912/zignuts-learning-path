const API_URL = "http://127.0.0.1:8000/api/auth/tasks/";
const token = sessionStorage.getItem("access");
const taskList = document.getElementById("taskList");
const taskModal = new bootstrap.Modal(document.getElementById("taskModal"));
const taskForm = document.getElementById("taskForm");

if (!token) window.location.href = "login.html";


const dueDateInput = document.getElementById("due_date");

function setMinimumDueDate() {
  const today = new Date();
  const year = today.getFullYear();
  const month = String(today.getMonth() + 1).padStart(2, "0");
  const day = String(today.getDate()).padStart(2, "0");

  dueDateInput.min = `${year}-${month}-${day}`;
}

setMinimumDueDate();

async function apiRequest(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
      ...options.headers
    }
  });
  if (response.status === 401) {
    sessionStorage.clear();
    window.location.href = "login.html";
    throw new Error("Session expired. Please log in again.");
  }
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(Object.values(error).flat().join(" ") || "Request failed.");
  }
  return response.status === 204 ? null : response.json();
}

function showMessage(text, type = "success") {
  document.getElementById("message").innerHTML = "";
  const alert = document.createElement("div");
  alert.className = `alert alert-${type}`;
  alert.textContent = text;
  document.getElementById("message").appendChild(alert);
}

async function loadTasks() {
  taskList.innerHTML = '<div class="col-12">Loading tasks...</div>';
  const params = new URLSearchParams();
  const search = document.getElementById("searchInput").value.trim();
  const status = document.getElementById("statusFilter").value;
  const priority = document.getElementById("priorityFilter").value;
  params.set("ordering", document.getElementById("sortOrder").value);
  if (search) params.set("search", search);
  if (status) params.set("status", status);
  if (priority) params.set("priority", priority);
  try {
    const tasks = await apiRequest(`${API_URL}?${params}`);
    taskList.innerHTML = "";
    if (tasks.length === 0) {
      taskList.innerHTML = '<div class="col-12"><div class="alert alert-info">No tasks found.</div></div>';
      return;
    }
    tasks.forEach(task => {
      const column = document.createElement("div");
      column.className = "col-md-6 col-lg-4";
      const card = document.createElement("div");
      card.className = "card h-100 shadow-sm";
      const body = document.createElement("div");
      body.className = "card-body";
      const title = document.createElement("h5");
      title.className = "card-title";
      title.textContent = task.title;
      const description = document.createElement("p");
      description.className = "text-secondary";
      description.textContent = task.description || "No description";
      const details = document.createElement("p");
      details.textContent = `Priority: ${task.priority} | Due: ${task.due_date}`;
      const status = document.createElement("span");
      status.className = `badge ${task.status === "completed" ? "bg-success" : "bg-warning text-dark"}`;
      status.textContent = task.status;
      const actions = document.createElement("div");
      actions.className = "d-flex flex-wrap gap-2 mt-3";
      const edit = document.createElement("button");
      edit.className = "btn btn-sm btn-outline-primary";
      edit.textContent = "Edit";
      edit.addEventListener("click", () => openEditModal(task));
      const complete = document.createElement("button");
      complete.className = "btn btn-sm btn-outline-success";
      complete.textContent = task.status === "completed" ? "Reopen" : "Complete";
      complete.addEventListener("click", () => toggleTask(task));
      const remove = document.createElement("button");
      remove.className = "btn btn-sm btn-outline-danger";
      remove.textContent = "Delete";
      remove.addEventListener("click", () => deleteTask(task.id));
      actions.append(edit, complete, remove);
      body.append(title, description, details, status, actions);
      card.appendChild(body);
      column.appendChild(card);
      taskList.appendChild(column);
    });
  } catch (error) {
    taskList.innerHTML = "";
    showMessage(error.message, "danger");
  }
}

function openEditModal(task = null) {
  taskForm.reset();
  document.getElementById("formError").textContent = "";
  document.getElementById("taskId").value = task?.id || "";
  document.getElementById("modalTitle").textContent = task ? "Edit Task" : "Add Task";
  document.getElementById("title").value = task?.title || "";
  document.getElementById("description").value = task?.description || "";
  document.getElementById("priority").value = task?.priority || "medium";
  document.getElementById("due_date").value = task?.due_date || "";
  taskModal.show();
}

taskForm.addEventListener("submit", async event => {
  event.preventDefault();
  const id = document.getElementById("taskId").value;
  const data = {
    title: document.getElementById("title").value.trim(),
    description: document.getElementById("description").value.trim(),
    priority: document.getElementById("priority").value,
    due_date: document.getElementById("due_date").value,
    status: "pending"
  };
  try {
    await apiRequest(id ? `${API_URL}${id}/` : API_URL, {
      method: id ? "PATCH" : "POST",
      body: JSON.stringify(data)
    });
    taskModal.hide();
    showMessage(id ? "Task updated successfully." : "Task created successfully.");
    loadTasks();
  } catch (error) {
    document.getElementById("formError").textContent = error.message;
  }
});

async function toggleTask(task) {
  try {
    await apiRequest(`${API_URL}${task.id}/`, {
      method: "PATCH",
      body: JSON.stringify({ status: task.status === "completed" ? "pending" : "completed" })
    });
    showMessage("Task status updated.");
    loadTasks();
  } catch (error) {
    showMessage(error.message, "danger");
  }
}

async function deleteTask(id) {
  if (!confirm("Are you sure you want to delete this task?")) return;
  try {
    await apiRequest(`${API_URL}${id}/`, { method: "DELETE" });
    showMessage("Task deleted successfully.");
    loadTasks();
  } catch (error) {
    showMessage(error.message, "danger");
  }
}

document.getElementById("addTaskBtn").addEventListener("click", () => openEditModal());
document.getElementById("logoutBtn").addEventListener("click", () => {
  sessionStorage.clear();
  window.location.href = "login.html";
});
document.getElementById("statusFilter").addEventListener("change", loadTasks);
document.getElementById("priorityFilter").addEventListener("change", loadTasks);
document.getElementById("sortOrder").addEventListener("change", loadTasks);
document.getElementById("searchInput").addEventListener("input", loadTasks);
loadTasks();