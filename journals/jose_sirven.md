# Development Journal

## Aug 15
On this day, we started the paired programming. We finally felt like we understood the overall strucutre of our app and our tech stack. We started by ensuring that our Docker-compose works.

## Aug 16
We wrote the migrations files and created the database file in docker. Then we updated the docker-compose file and added the database service. Next we started building our migrations for our PostgreSQL.  We had to edit the foreign keys as constraints and had to takedown the new tables. We were told we need to a separate migration file for each table.

## Aug 17
Today, we started by creating the separate migration files. Dom was driving the coding today.

## Aug 21
We built the get and update endpoints. I felt a lot more confident understanding how FastAPI works high-level - how the queries and the routers interact with each other.

## Aug 22
Built out the endpoints using FastAPI for my plans story. We started working on the backend auth for logged in users. We got stuck but got help from Phil & Dalonte.

## Aug 23
We finished the backend Auth. Were having issues passing the id to the return user function when calling the POST request with the hashed password.

## Aug 24
We were finally able to get the backend auth working & get the newly created user object returned with hashed password when calling the POST request. Then we created protected routes for logged in users. We created a plan for the frontend.

## Aug 28
It was my first day of leading - felt confident. I held a stand-up and took notes and we set goals. I also learned expressive library that handles state really easily for react. We created the react routes together and then assigned the individual components to each other. I learned a new library called expressive.

## Aug 29
I researched the trip advisor api. Made the fetchwrapper. Learned hwo to properly use the global variables for the environment in .env. Decided to build the top destinations as a separate component to import into the homepage. I also built the query search bar that alters the query variable and rerenders the component when the query changes.
