# Development Journal

## Aug 15
On this day, we started the paired programming. We finally felt like we understood the overall strucutre of our app and our tech stack. We started by ensuring that our Docker-compose works.

## Aug 16
We wrote the migrations files and created the database file in docker. Then we updated the docker-compose file and added the database service. Next we started building our migrations for our PostgreSQL.  We had to edit the foreign keys as constraints and had to takedown the new tables. We were told we need to a separate migration file for each table.

## Aug 17
Today, we started by creating the separate migration files. Dom was driving the coding today.

## Aug 21
We built the get and update endpoints. I felt a lot more confident understanding how FastAPI works high-level - how the queries and the routers interact with each other.

## Sept 5
I focused getting the TripAdvisor API to work, but kept running into CORS issues. I tried getting Violet's help, but we couldn't figure it out. After hours of troubleshooting, the team and I agreed to move on to the nav bar. Using code from a past project as an example, I built out the nav bar and made it so that whenever the token was present login/sign up was hidden.

## Sept 6
Today, I added the logout functiontionality. Then I started working on the unit tests.
