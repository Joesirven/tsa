steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(50) UNIQUE NOT NULL,
            hashed_password VARCHAR(500) NOT NULL
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
            monthly_budget DECIMAL(7,2) CHECK (monthly_budget > 0) NOT NULL,
            users_id SERIAL NOT NULL,
            CONSTRAINT fk_users_id FOREIGN KEY(users_id) REFERENCES users(id) ON DELETE CASCADE
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
            plans_id SERIAL NOT NULL,
            CONSTRAINT fk_plans_id FOREIGN KEY(plans_id) REFERENCES plans(id) ON DELETE CASCADE,
            current_amount_saved DECIMAL(7,2) CHECK (current_amount_saved >= 0) NOT NULL,
            final_goal_amount DECIMAL(7,2) CHECK (final_goal_amount >= 0) NOT NULL,
            if_saved BOOLEAN DEFAULT FALSE NOT NULL
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
            savings_id SERIAL NOT NULL,
            CONSTRAINT fk_savings_id FOREIGN KEY(savings_id) REFERENCES savings(id) ON DELETE CASCADE,
            amount_saved DECIMAL(7,2),
            date TIMESTAMPTZ
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
            cost DECIMAL(7,2) CHECK (cost > 0) NOT NULL,
            plans_id SERIAL NOT NULL,
            CONSTRAINT fk_plans_id FOREIGN KEY(plans_id) REFERENCES plans(id) ON DELETE CASCADE,
            paid BOOLEAN DEFAULT FALSE NOT NULL,
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
            name VARCHAR(100),
            expenses_id SERIAL NOT NULL,
            CONSTRAINT fk_expenses_id FOREIGN KEY(expenses_id) REFERENCES expenses(id) ON DELETE CASCADE
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
            date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            users_id SERIAL NOT NULL,
            CONSTRAINT fk_users_id FOREIGN KEY(users_id) REFERENCES users(id) ON DELETE CASCADE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE journals;
        """
    ],

]
