from django.urls import path
from core import views

from core.views import (
    apiOverview,
    taskList,
    taskDetail,
    taskCreate,
    taskUpdate,
    taskDelete,
)

urlpatterns = [
    path("", apiOverview, name="api-overview"),
    path("task-list/", taskList, name="task-list"),
    path("task-detail/<int:pk>/", taskDetail, name="task-detail"),
    path("task-create/", taskCreate, name="task-create"),
    path("task-update/<int:pk>/", taskUpdate, name="task-update"),
    path("task-delete/<int:pk>/", taskDelete, name="task-delete"),
]
