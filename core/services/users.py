from typing import List

from django.db import models

from core.models import BaseUser, Employee, Businessman, Courier, FoodOrder


def get_concrete_user(user: BaseUser) -> models.Model or None:
    """Метод для того, чтобы вернуть конкретный экземпляр
    пользователя"""
    for Instance in [Employee, Businessman, Courier]:
        queryset = Instance.objects.filter(user_id=user.user_id)
        if queryset:
            return queryset.get()

    return None


def get_addresses(employee: Employee) -> List[models.Model]:
    """Функция для получения списка адресов пользователя"""
    return employee.addresses.all()


def get_emp_orders(employee: Employee, orders_count: int or None = None) -> List[models.Model]:
    """Функция для получения последних заказов клиента,
    отсортированных по времени в порядке убывания

    :param employee: модель работника, чьи заказы рассматриваются
    :param orders_count: количество заказов, которые надо получить.
    Если None, то получить все заказы

    :returns: Возвращает список моделей заказов"""
    if orders_count:
        return employee.foodorder_set.order_by('-time').all()[:orders_count]
    return employee.foodorder_set.order_by('-time').all()


def get_courier_orders(courier: Courier, orders_count: int or None = None) -> List[models.Model]:
    """Функция для получения последних заказов, выполненных курьером,
    отсортированных по времени в порядке убывания

    :param courier: модель рассматриваемого курьера
    :param orders_count: количество заказов, которые надо получить.
    Если None, то получить все заказы

    :returns: Возвращает список моделей заказов"""
    if orders_count:
        return courier.foodorder_set.order_by('-time').all()[:orders_count]

    return courier.foodorder_set.order_by('-time').all()


def get_profile_context(base_user: BaseUser) -> dict:
    """Метод для того, чтобы вернуть контекст для profile_view"""
    user = get_concrete_user(base_user)
    if type(user) is Employee:
        return {
            'user_type': 'Employee',
            'addresses': get_addresses(user),
            'orders': get_emp_orders(user, 5),
            'company': user.company
        }

    elif type(user) is Businessman:
        return {
            'user_type': 'Businessman',
            'market': user.market
        }
    elif type(user) is Courier:
        return {
            'user_type': 'Courier',
            'orders': get_courier_orders(user, 5),
            'market': user.chief.market
        }
    else:
        return {
            'user_type': 'Admin'
        }
