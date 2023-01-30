# CSS-Clips

An app where users can view a database of user created CSS animations in a grid display.
(Giphy, but for CSS animations.)

## MVP Goals
 -   Django, Python, SQL tech stack
 -   grid of window frames that each display a simple CSS animation
 -   full CRUD for user's own clips
 -   each animation has tags
 -   search bar
        -   can search by clip title
 - each CSS clip renders on its own detail page
 - basic Bulma styling for site

## Stretch Goals
- Many to Many relationship (tags -> clips)
- Search Bar allows search by clip title AND tag
- smooth looking Bulma styling for site
- query results page displays grid of many divs w/ CSS animations happening at once (like Giphy)
- "trending" CSS clips on index page
- user ability to save favorites, view them on user's detail page

## User Stories
My user is someone who wants to find and share small CSS animations for use on their own websites. For styling my own pages, I've found a lot of inspiration by seeing cool animations from other sites around the web. But there's no destination to find a LOT of them all at once. I had this vision of a site like Giphy, that displays CSS animations in a way where it's easy to see a lot of them, and then reference the code to learn and adapt it for my own use. I haven't found it. So I figured I'd have to make it, myself. And I'm thinking there are a lot of other people who may feel the same as me.

-   user can view index route of all clips
-   user can search for clips by title
-   user can view clips by difficulty level
-   user can login (auth)
-   user can add, edit, delete own clips
-   user can favorite others' animations
-   user can view their own favorites on own profile detail route

## Milestones
### Day 1
- Create data Models, views, urls in Django
- Create PostGreSQL db
### Day 2
- Generate seed data, 
- seed DB
- add auth to site
### Day 3
- Deploy SQL db, integrate with frontend
### Day 4
- Styling, bug squashing
### Day 5
- Deploy, additional styling, stretch goals

## Initial Wireframes
[Figma](https://www.figma.com/file/g76YgWIyT3rpwRORYhhRxl/CSSclips?node-id=0%3A1&t=CbeFnI6NZkVwaiTI-1 "Figma")
![Desktop Wireframe](assets/planning-images/css-clips-wireframe-desktop.png)
![Mobile Wireframe](assets/planning-images/css-clips-wireframe-mobile.png)

## ERD

-   [Lucid ERD](https://lucid.app/lucidchart/5f8c4e99-2a6d-4141-9767-383d972d3539/edit?viewport_loc=-133%2C181%2C1936%2C1024%2C0_0&invitationId=inv_b147fe33-04b3-4390-87c7-63998297fbd9, "Lucid ERD")
![CSS Clips ERD](assets/planning-images/css-clips-erd.png)

## Summary
-   Tech Stack:
    -   Django/Python
-   App Summary:
    -   CSS-Giphy: An app where users can view a database of user created CSS animations in a grid display
-   Key Features:
    -   Users can search by animation title
    -   Users can create animations
-   Stretch Features:
    -   Auth/login for users
    -   Users can update and destroy own animations
    -   Users can add tags to their animations
    -   Users can search by tags
    -   Users can favorite an animation
        -   view their favorites collection