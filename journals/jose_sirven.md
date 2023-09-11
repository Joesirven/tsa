# Development Journal

## Sept 11
Over the weekend, I finally figured out the unit test thanks to Dom's help. I merged it to the main branch this morning.

## Sept 8
I figured out how to redirect after they log in back to the original page that someone wanted to go to. This was tricky. I had to get Violet's help.

Then Dom and I started working on the unit tests but we ran out of time for the day.

## Sept 7
I protected all of our routes on the front end using the router browser. It took a while because everyone had a different way of doing it. Eventually, Violet shared a way to do it that worked for me really well. Within the main app, I created another component called ProtectedRoute that tested for a token and then used conditional logic to either navigate to the login/ page or to the child of the ProtectedRoute component. Wayne helped with this too.

## Sept 6
Today, I added the logout functiontionality. Then I started working on the unit tests.

## Sept 5
I focused getting the TripAdvisor API to work, but kept running into CORS issues. I tried getting Violet's help, but we couldn't figure it out. After hours of troubleshooting, the team and I agreed to move on to the nav bar. Using code from a past project as an example, I built out the nav bar and made it so that whenever the token was present login/sign up was hidden.

## Aug 28
Today, i met with my friend Gabe who created a library tohandle state management for react components. It's called expressive and really saves a lot of time.

Today, I also started working on the MainPage Component. I started reading about 3rd Party API's on the fronted end and specifically the trip advisor one.

## Aug 25
Today, I built out the strucutre of the HomePage. We divded the different pages among us and started workign on the components individually.

My components were the HomePage and the sign in and sign out pages. I know I had to add additional functionality to those. I also knew that I had to figure out the nav bar cause it changes depending on whether someone is logged in or out.

## Aug 24
After getting the token working, we were able to add the user_data object to the argument to protect the routes.
At first we thought you had to do more, but realized that just being adding the argument - the route wouldn't run without it.

We tested each of the routes using swagger logged in and logged out and they all worked.

## Aug 23
We're finally starting to get somewhere with the backend authentication. We followed the videos to the t, but there's a gap in one of the videos that we needed to figure out.

Phil the seir, helped us out. Delonte came into the room and started guiding us towards the end of the day. We finally figured out that the problem was that the create method wasn't being called and the SQL command wasn't indented incorrectly.

## Aug 22
We started working on the back-end auth. We originally started working individually but then realized it'd be easier if we worked together towards the end of the day.

## Aug 21
We built the get and update endpoints. I felt a lot more confident understanding how FastAPI works high-level - how the queries and the routers interact with each other.

## Aug 17
Today, we started by creating the separate migration files. Dom was driving the coding today.

## Aug 16
We wrote the migrations files and created the database file in docker. Then we updated the docker-compose file and added the database service. Next we started building our migrations for our PostgreSQL.  We had to edit the foreign keys as constraints and had to takedown the new tables. We were told we need to a separate migration file for each table.

## Aug 15
On this day, we started the paired programming. We finally felt like we understood the overall strucutre of our app and our tech stack. We started by ensuring that our Docker-compose works.
