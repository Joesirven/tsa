steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE user (
            id SERIAL PRIMARY KEY NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            password_confirmation CHKPASS
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE user;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE plans (
            id SERIAL PRIMARY KEY NOT NULL,
            start_of_budget TIMESTAMP NOT NULL,
            end_of_budget TIMESTAMP NOT NULL,
            trip_duration INTERVAL NOT NULL,
            trip_start_date TIMESTAMP NOT NULL,
            automatically_set_date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            required_integer INTEGER NOT NULL,
            required_money MONEY NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE plans;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE savings (
            id SERIAL PRIMARY KEY NOT NULL,
            plans_id FOREIGN KEY NOT NULL ON DEL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE savings;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE transactions (
            id SERIAL PRIMARY KEY NOT NULL,
            required_limited_text VARCHAR(1000) NOT NULL,
            required_unlimited_text TEXT NOT NULL,
            required_date_time TIMESTAMP NOT NULL,
            automatically_set_date_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            required_integer INTEGER NOT NULL,
            required_money MONEY NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE transactions;
        """
    ],
        [
        # "Up" SQL statement
        """
        CREATE TABLE expenses (
            id SERIAL PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            cost INTEGER NOT NULL,
            required_integer INTEGER NOT NULL,
            paid TIMESTAMP NOT NULL,
            type TEXT NOT NULL,
            required_money MONEY NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE expenses;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE journal (
            id SERIAL PRIMARY KEY NOT NULL,
            location VARCHAR(50) NOT NULL,
            picture_url VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            password_confirmation CHKPASS
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE journal;
        """
    ],

]
