from app.database import get_db


class MemoryService:

    @staticmethod
    def save_message(
        session_id,
        role,
        content
    ):
        db = get_db()

        cursor = db.cursor()

        cursor.execute(
            """
            INSERT INTO messages
            (
                session_id,
                role,
                content
            )
            VALUES(?,?,?)
            """,
            (
                session_id,
                role,
                content
            )
        )

        db.commit()
        db.close()

    @staticmethod
    def get_history(
        session_id
    ):
        db = get_db()

        cursor = db.cursor()

        cursor.execute(
            """
            SELECT role,content
            FROM messages
            WHERE session_id=?
            ORDER BY id ASC
            """,
            (session_id,)
        )

        rows = cursor.fetchall()

        db.close()

        return [
            {
                "role": x[0],
                "content": x[1]
            }
            for x in rows
        ]

    @staticmethod
    def get_sessions():

        db = get_db()

        cursor = db.cursor()

        cursor.execute(
            """
            SELECT DISTINCT session_id
            FROM messages
            """
        )

        rows = cursor.fetchall()

        db.close()

        return [
            row[0]
            for row in rows
        ]

    @staticmethod
    def delete_history(
        session_id
    ):
        db = get_db()

        cursor = db.cursor()

        cursor.execute(
            """
            DELETE FROM messages
            WHERE session_id=?
            """,
            (session_id,)
        )

        db.commit()
        db.close()
