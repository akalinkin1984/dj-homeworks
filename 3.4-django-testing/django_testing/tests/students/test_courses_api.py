import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    course = course_factory(_quantity=1)
    url = reverse('courses-list')

    response = client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert len(course) == len(data)
    assert data[0]['name'] == course[0].name


@pytest.mark.django_db
def test_get_list_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse('courses-list')

    response = client.get(url)
    data = response.json()

    assert response.status_code == 200
    assert len(courses) == len(data)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_check_filter_courses_id(client, course_factory):
    courses = course_factory(_quantity=10)

    url = reverse('courses-list')
    response = client.get(url, {'id': courses[5].id})
    data = response.json()

    assert response.status_code == 200
    assert data[0]['id'] == courses[5].id


@pytest.mark.django_db
def test_check_filter_courses_name(client, course_factory):
    courses = course_factory(_quantity=10)

    url = reverse('courses-list')
    response = client.get(url, {'name': courses[3].name})
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == courses[3].name


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    data = {'name': 'course1'}
    url = reverse('courses-list')

    response = client.post(url, data=data)

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)
    new_data = {'name': 'new course'}
    url = reverse('courses-list')
    print(url)
    response = client.patch(url + f'{course[0].id}', data=new_data)
    data = response.json()

    assert response.status_code == 301
    assert data[0]['name'] == course[0].name


# @pytest.mark.django_db
# def test_delete_course(client, course_factory):
#     course = course_factory(_quantity=1)
#     new_data = {'name': 'new course'}
#     url = reverse('courses-list')
#
#     response = client.patch(url + f'/{course[0].id}/', data=new_data)
#     data = response.json()
#
#     assert response.status_code == 204
#     assert data[0]['name'] == course[0].name
