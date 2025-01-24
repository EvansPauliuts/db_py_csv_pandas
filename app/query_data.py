queries = [
    {
        'name': 'Сотрудники и их отделы',
        'query': """
            SELECT e.employee_name, d.department_name
            FROM employee e
            JOIN department d ON e.department_id = d.department_id;
        """,
    },
    {
        'name': 'Сотрудники и их профессии',
        'query': """
            SELECT e.employee_name, j.job_title
            FROM employee e
            JOIN job j ON e.job_id = j.job_id;
        """,
    },
    {
        'name': 'Сотрудники и их бонусы',
        'query': """
            SELECT e.employee_name, b.bonus_amount
            FROM employee e
            JOIN bonus b ON e.employee_id = b.employee_id;
        """,
    },
    {
        'name': 'Все данные о сотрудниках',
        'query': """
            SELECT e.employee_name, d.department_name, j.job_title, b.bonus_amount
            FROM employee e
            JOIN department d ON e.department_id = d.department_id
            JOIN job j ON e.job_id = j.job_id
            LEFT JOIN bonus b ON e.employee_id = b.employee_id;
        """,
    },
]
