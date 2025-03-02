<h1 align="center">🥃 <a href="https://dialysisdiary-b28cf5143cfa.herokuapp.com/">Dialysis Connect</a> 🥃</h1>

![Responsiveness](images_documentation/lighthouse_scores/responsive.png)

## Dialysis Connect is a web-based platform designed to support individuals undergoing dialysis treatment by providing essential tools to manage their medical journey effectively. The platform aims to foster a supportive community, streamline record-keeping, and offer accessible features that enhance the overall patient experience. It serves as a comprehensive solution for dialysis patients to log their health records, schedule important events, share experiences, and store medical documents securely.

### Key features:

1. Community Forum:

    - Users can share experiences and seek support from other dialysis patients.
    - Ability to create posts and comment on discussions.
    - Posts include timestamps and are displayed in reverse chronological order.
    - Users can edit or delete their own posts.

2. Dialysis Records Management:

    - Users can log essential dialysis details such as weight, blood pressure, fluid intake, and dwell times.
    - Ability to add comments for additional notes.
    - Records are automatically dated and displayed in reverse chronological order.    

3. Calendar and Event Scheduling:

    - Users can schedule and track hospital appointments or general reminders.
    - Events include start and end times to ensure proper scheduling.    

4. Document Uploads and Management:

    - Users can securely upload and store important medical documents, prescriptions, and reports.
    - Custom naming options for easy identification of uploaded files.
    - Cloud storage integration via Cloudinary ensures secure access to documents.

5. User Authentication and Security:

    - Secure user registration and login functionality.
    - Users can only access and modify their own records and uploads.
    - Enforced password validation and authentication best practices.

6. Responsive and Accessible Design:

    - Mobile-friendly interface to ensure accessibility across devices.
    - Compliance with accessibility standards to cater to users with disabilities.

7. Dashboard Overview:

    - A central dashboard displaying quick links to community posts, dialysis records, calendar events, and uploaded documents.
    - Intuitive navigation for seamless user experience.

[User Stories](#user-stories)

[User Experience](#user-experience)

- [Typography & Colors](#typography--color-scheme)
- [Agile planning](#agile-planning)
- [Features](#features)

[Wireframes](#wireframes)

- [Database design](#database-design)

[Technology stack](#technology-stack)

- [Tools used](#tools-used)

[Migration from Gitpod to VS code](#migration)

[Fixed bugs](#fixed-bugs)

[Testing](#testing)

[Deployment](#deployment)

- [Via Heroku](#via-heroku)
- [Via Forking](#via-forking)

[Credits](#credits)

- [Media](#media)

## [User Stories]

### 1. Sign-up feature

- **As a** new user, **I want** to create an account **so that** I can access personalized features.
- **Acceptance**: Users enter email, username, and password. Errors show for taken usernames/emails.

### 2. Sign-in feature

- **As a** returning user, **I want** to log in to my account **so that** I can access my personalized data.
- **Acceptance**: Users log in using their email and password and authentication fails if credentials are invalid

### 3. View posts

- **As a** logged-in user, **I want** to view posts shared by others, **so that** I can engage with the community.
- **Acceptance**: Users can see a list of posts with each post showing the author, content and timestamp.

### 4. Submit a post

- **As a** logged-in user, **I want** to submit a post, **so that** I can share my experiences with the community.
- **Acceptance**: Users can type and submit new posts.

### 5. Edit a post

- **As a** logged-in user, **I want** to edit my existing posts, **so that** I can correct or update the content.
- **Acceptance**: Users can only edit their own posts.

### 6. Delete a post

- **As a** logged-in user, **I want** to delete my posts, **so that** I can remove content I no longer want to share.
- **Acceptance**: Users can only delete their own posts.

### 7. Add a dialysis record

- **As a** dialysis patient, **I want** to record my dialysis session details, **so that** I can track my treatment history over time.
- **Acceptance**: The user must be logged in to add a record and the form should contain all the necessary fields.

### 8. View past records

- **As a** dialysis patient, **I want** to view my past dialysis records, **so that** I can analyze my treatment trends over time.
- **Acceptance**: The user must be logged in to view records and can only view their own records.

### 9. Calendar

- **As a** dialysis patient, **I want** to see a calendar displaying my appointments and reminders, **so that** I can manage my dialysis-related schedule efficiently.
- **Acceptance**: The user must be logged in to access the calendar, the calendar should display a monthly view by default, and clicking on a date should show a list of events for that day.

### 10. Add an event or appointment

- **As a** dialysis patient, **I want** to add an appointment or reminder to my calendar, **so that** I can keep track of important events related to my treatment.
- **Acceptance**: The user must be logged in to add an event. The form should validate required fields and display error messages for missing/invalid inputs, the event should be saved in the database upon submission, and the user should receive a confirmation message after saving the event.

### 11. Edit calendar event

- **As a** dialysis patient, **I want** to edit an existing event, **so that** I can update details if needed.
- **Acceptance**: The user must be logged in to edit an event and the user can only edit their own events.

### 12. Delete calendar event

- **As a** dialysis patient, **I want** to delete an event, **so that** I can remove unnecessary or incorrect entries.
- **Acceptance**: The user must be logged in to delete an event and the user can only delete their own events.
### 13. Upload document

- **As a** dialysis patient, **I want** to upload and store important documents (e.g., prescriptions, reports), **so that** I can easily access them whenever needed.
- **Acceptance**: The user must be logged in to upload, view, or delete documents. The upload form should accept PDF, PNG, and JPEG file formats. The maximum file size should be 5MB to prevent excessive storage usage.

## User Experience

### Typography & Color scheme



### Agile Planning



### Features


### Wireframes



### Database design

The database was designed to allow CRUD functionality to registered users.

The ERD (Entity Relationship Diagram) was designed on [dbdiagram.io](https://dbdiagram.io/d/DialysisConnect-67c39901263d6cf9a0e91d6d)

  

### Tools used

- Git: Used commands such as `git` `add` - `commit -m "message'` - `push`.
- VS code: Used as my IDE.
- Github: Used as the code hosting.
- [Font awesome](https://fontawesome.com/): Used for a variety of icons through the pages.
- [Favicon io](https://favicon.io/favicon-converter/): Used to generate the faveicon.
- [Balsamiq](https://balsamiq.com/wireframes/desktop/): Used to create the wireframes - desktop version.
- [TinyPNG](https://tinypng.com/): Used to compress each image used in the project for optimal load times.
- [dbdiagraim.io](https://dbdiagram.io/home): Used to create the ERD.
- [GSAP](https://gsap.com/): Used for the animations on the 404 page.

## Migration from Gitpod to VS code


## Fixed bugs



## Testing

For a detailed overview of both manual and automated testing processes, please refer to [TESTING.md](https://github.com/NontyD/dialysis_diary/blob/main/TESTING.md). It covers all testing scenarios and methodologies used in the project.

## Deployment

### via Heroku

1. Navigate to [heroku](https://www.heroku.com/home) and create an account.
2. Click `Create new app`, enter the app name and choose your region, hit `create app`.
3. Click **Deploy** and in the _Deployment method_ option choose **Github**. Enter the repository's name and click connect, you can leave the branch deployment to `main`.
   > You need to have created your github repository.
4. Head to **Settings** and click `Reveal config vars`
5. On the KEY inputs add: DATABASE_URL - SECRET_KEY - CLOUDINARY_URL. On the VALUE inputs add your own, for each one.
6. Click **Add buildpack** and choose `python`.
7. Now you're set. Go back to `Deploy` and click **Deploy branch**.


### Via Forking

1. Click the **Fork** button at the top right of the repository page.
2. This will create a copy of the repository in your own GitHub account, which you can modify independently.

## Credits


[ChatGPT 4o](https://openai.com/chatgpt/) / [Codeium](https://codeium.com/) / [Stack Overflow](https://stackoverflow.com/) for adjustments and bug fixing aid.

The main idea for this project was obtained by the [Django Blog](https://www.youtube.com/watch?v=YH--VobIA8c) walkthrough project of the [Code Institute course](https://codeinstitute.net/global/).

### Media

All photos used in the project - including favicon - were taken from [Pexels](https://www.pexels.com/) / [Unsplash](https://unsplash.com/) / [Freepik](https://www.freepik.com/).