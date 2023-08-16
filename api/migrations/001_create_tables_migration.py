steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            password_confirmation VARCHAR(50) NOT NULL,
            CONSTRAINT password_match CHECK (password = password_confirmation)
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE plans (
            id SERIAL PRIMARY KEY NOT NULL,
            start_of_budget TIMESTAMPTZ NOT NULL,
            end_of_budget TIMESTAMPTZ NOT NULL,
            trip_start_date TIMESTAMPTZ NOT NULL,
            trip_end_date TIMESTAMPTZ NOT NULL,
            destination VARCHAR(100) NOT NULL,
            monthly_budget DECIMAL(7,2) UNSIGNED CHECK (monthly_budget > 0) NOT NULL,
            users_id FOREIGN KEY REFERENCES users(id) NOT NULL
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
            plans_id FOREIGN KEY REFERENCES plans(id) NOT NULL,
            current_amount_saved DECIMAL(7,2) UNSIGNED CHECK (current_amount_saved > 0) NOT NULL,
            final_goal_amount DECIMAL(7,2) UNSIGNED CHECK (final_goal_amount > 0) NOT NULL,
            if_saved BOOLEAN DEFAULT 0 NOT NULL
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
            savings_id FOREIGN KEY REFERENCES savings(id) NOT NULL ON DELETE CASCADE

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
            name VARCHAR(100) NOT NULL,
            cost DECIMAL(7,2) UNSIGNED CHECK (cost > 0) NOT NULL,
            plans_id FOREIGN KEY REFERENCES plans(id) NOT NULL,
            paid BOOLEAN DEFAULT 0 NOT NULL,
            type VARCHAR(50) NOT NULL
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
        CREATE TABLE expenses_type_vo (
            id SERIAL PRIMARY KEY NOT NULL,
            name FOREIGN KEY REFERNCES expenses(id) NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE expenses_type_vo;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE journals (
            id SERIAL PRIMARY KEY NOT NULL,
            location VARCHAR(50) NOT NULL,
            picture_url VARCHAR(100) NOT NULL,
            description VARCHAR(200) NOT NULL,
            rating INTEGER CHECK (rating >= 1 AND rating <= 5) NOT NULL,
            date TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE journals;
        """
    ],

]
