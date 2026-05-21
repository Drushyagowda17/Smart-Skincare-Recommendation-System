REMINDER_DEFAULTS = {
    'morning': '07:00',
    'night': '21:00'
}


def get_reminders(user_id, db_conn):
    cursor = db_conn.execute(
        "SELECT * FROM reminders WHERE user_id = ?",
        (user_id,)
    )
    reminders = [dict(row) for row in cursor.fetchall()]

    if not reminders:
        reminders = [
            {'id': None, 'user_id': user_id, 'routine_type': 'morning', 'time': '07:00', 'enabled': 1},
            {'id': None, 'user_id': user_id, 'routine_type': 'night', 'time': '21:00', 'enabled': 1}
        ]

    return reminders


def save_reminder(user_id, routine_type, time, enabled, db_conn):
    cursor = db_conn.execute(
        "SELECT id FROM reminders WHERE user_id = ? AND routine_type = ?",
        (user_id, routine_type)
    )
    existing = cursor.fetchone()

    if existing:
        db_conn.execute(
            "UPDATE reminders SET time = ?, enabled = ? WHERE id = ?",
            (time, enabled, existing['id'])
        )
    else:
        db_conn.execute(
            "INSERT INTO reminders (user_id, routine_type, time, enabled) VALUES (?, ?, ?, ?)",
            (user_id, routine_type, time, enabled)
        )
    db_conn.commit()


def toggle_reminder(reminder_id, db_conn):
    cursor = db_conn.execute(
        "SELECT enabled FROM reminders WHERE id = ?",
        (reminder_id,)
    )
    reminder = cursor.fetchone()
    if reminder:
        new_status = 0 if reminder['enabled'] else 1
        db_conn.execute(
            "UPDATE reminders SET enabled = ? WHERE id = ?",
            (new_status, reminder_id)
        )
        db_conn.commit()
        return new_status
    return None
