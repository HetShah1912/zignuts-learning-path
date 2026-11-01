from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskManagerAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="TestPass123!"
        )

        # Create a task belonging to that user
        self.task = Task.objects.create(
            user=self.user,
            title="Learn DRF",
            description="Practice API development",
            due_date="2026-11-10",
            priority="High",
            status="Pending"
        )

        # Obtain a real JWT access token
        response = self.client.post(
            reverse("token_obtain_pair"),
            {
                "username": "testuser",
                "password": "TestPass123!"
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.access_token = response.data["access"]
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

    def test_list_tasks(self):
        response = self.client.get(reverse("task-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Learn DRF")

    def test_create_task(self):
        data = {
            "title": "Build a project",
            "description": "Create a Task Manager API",
            "due_date": "2026-11-15",
            "priority": "Medium",
            "status": "Pending"
        }

        response = self.client.post(
            reverse("task-list"), data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(response.data["title"], "Build a project")

        created_task = Task.objects.get(title="Build a project")
        self.assertEqual(created_task.user, self.user)

    def test_retrieve_task(self):
        response = self.client.get(
            reverse("task-detail", args=[self.task.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Learn DRF")

    def test_update_task(self):
        data = {
            "title": "Learn advanced DRF",
            "description": "Practice serializers and viewsets",
            "due_date": "2026-11-20",
            "priority": "Medium",
            "status": "In Progress"
        }

        response = self.client.put(
            reverse("task-detail", args=[self.task.id]),
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Learn advanced DRF")
        self.assertEqual(self.task.status, "In Progress")

    def test_delete_task(self):
        response = self.client.delete(
            reverse("task-detail", args=[self.task.id])
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_unauthenticated_user_cannot_list_tasks(self):
        self.client.credentials()

        response = self.client.get(reverse("task-list"))

        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN]
        )

    def test_user_cannot_access_another_users_task(self):
        another_user = User.objects.create_user(
            username="anotheruser",
            password="AnotherPass123!"
        )

        another_task = Task.objects.create(
            user=another_user,
            title="Private task",
            description="This belongs to another user",
            due_date="2026-11-12",
            priority="Low",
            status="Pending"
        )

        response = self.client.get(
            reverse("task-detail", args=[another_task.id])
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_jwt_login(self):
        response = self.client.post(
            reverse("token_obtain_pair"),
            {
                "username": "testuser",
                "password": "TestPass123!"
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
