<h1 align="center"><a href="https://dialysisdiary-b28cf5143cfa.herokuapp.com/">Dialysis Connect</a></h1>

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/NontyD/dialysis_diary)](https://github.com/NontyD/dialysis_diary/commits/main)

[![GitHub last commit](https://img.shields.io/github/last-commit/NontyD/dialysis_diary)](https://github.com/NontyD/dialysis_diary/commits/main)

[![GitHub repo size](https://img.shields.io/github/repo-size/NontyD/dialysis_diary)](https://github.com/NontyD/dialysis_diary)


![Home](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741395866/website_jigf7b.png)

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

[Migration from Gitpod to VS code](#migration-from-gitpod-to-vs-code)

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

### Patient-Centered Approach

The design of Dialysis Connect is based on firsthand experience as a dialysis patient, focusing on features that are most relevant and beneficial. Informal feedback was gathered from fellow patients during hospital visits, providing valuable insights into usability and functionality.

### Color Scheme & Imagery

The Dialysis Connect website employs a minimalist and calming color palette to ensure a non-distracting and informative experience. The overall design approach ensures that Dialysis Connect remains an informative and functional platform, where content is the focal point, and aesthetics serve to support usability rather than overshadow it.

### Agile Planning



### Features

#### Home
![Home](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741395818/home_p6pzlp.png)

The Home page serves as the entry point for Dialysis Connect. It provides an introduction to the platform and a user-friendly interface to navigate different features. The page includes a welcome message, links to the Irish Kidney Association (IKA) for educational resources, and a navigation bar for seamless movement between sections.

#### Sign Up & Login
<p align="center">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741395847/signup_lmimdx.png" width="45%">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741395833/login_slbfps.png" width="45%">
</p>


Users must create an account to access the platform’s features.

    - Sign Up: New users can register by providing their details, such as email and password.
    - Login: Registered users can securely log in using their credentials.
    - User authentication ensures privacy and security while managing personal health information.

#### Dashboard
![Dashboard](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741209614/dashboard_bcciea.png)

After logging in, users are directed to the Dashboard, which provides an overview of the platform. The dashboard contains four main sections, each represented as a card:

    Community – Users can find support and share experiences.
    Records – Provides access to dialysis records and logs.
    Calendar – Displays appointments and reminders.
    Upload Documents – Allows users to store important medical documents.

The dashboard offers a simple, clean interface for users to quickly access the most relevant features.

#### Community
![Community](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741209614/community_hkjab1.png)

The Community section is a discussion space where users can share their experiences and seek support.

    Users can create and submit posts.
    Posts display the author, timestamp, and content.
    Posts are shown in reverse chronological order (newest first).
    Logged-in users can edit or delete their own posts.
    Empty posts are not allowed, ensuring meaningful discussions.

This section fosters a supportive environment for patients undergoing dialysis and their caregivers.

#### Dialysis Records
<p align="center">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741209614/add-records_qt41bx.png" width="45%">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741209615/records_hok3qg.png" width="45%">
</p>

The Records section acts as a dialysis diary, allowing users to log daily treatment details. Users can input:

    Weight before Dialysis (kg)
    Blood Pressure (systolic & diastolic)
    Initial Drain Volume (ml)
    Total UF (ml)
    Average Dwell (hh:mm)
    Lost Dwell (hh:mm)
    Added Dwell (hh:mm)
    Weight after Dialysis (kg)
    Comments for additional notes.

Users can retrieve and review past records, this helps users track treatment trends and communicate effectively with healthcare providers.

#### Calendar
![Calendar](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741209615/calendar_ylqemj.png)

The Calendar feature enables users to manage their hospital appointments and reminders.

    - Users can add events with a title, date, and description.
    - The calendar is displayed in a monthly view, along with a list of upcoming events.
    - Events can be edited or deleted as needed.
    
This feature ensures that users stay on top of their medical schedule and dialysis routine.

#### File Upload
<p align="center">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741209615/upload_kn12dn.png" width="45%">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741209615/files_diq2cy.png" width="45%">
</p>

Users can upload and store important documents such as prescriptions, medical reports, and test results.

    - Supports PDFs and images for convenience.
    - Users can name each uploaded file for easy identification.
    - Uploaded files remain accessible for future reference.

This feature acts as a digital medical file cabinet, allowing users to keep important records in one place.

#### Navigation Bar
![Nav bar - user not logged in](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741396439/nav-loogout_z5tz1a.png)
![Nav bar - user logged in](https://res.cloudinary.com/dzibrzlq9/image/upload/v1741396438/nav-login_oss0gk.png)

The Navigation Bar provides easy access to all sections of the platform.

    - Available on all pages, allowing users to switch between features without hassle.
    - Contains links to Community, Records, Calendar, Upload Documents, and Dashboard.


### Wireframes

#### Home and Dashboard
<p align="center">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741657095/wireframe_home_qojpwl.png" width="45%">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741657094/wireframe_dashboard_ab2mdl.png" width="45%">
</p>

#### Sign up and Login
<p align="center">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741657095/wireframe_signup_czdfhp.png" width="45%">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741657095/wireframe_login_yiyf8p.png" width="45%">
</p>

#### Community and Calendar
<p align="center">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741657094/wireframe_community_qbfy4i.png" width="45%">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741657094/wireframe_calendar_tanpo9.png" width="45%">
</p>

#### File uploads and Uploaded files
<p align="center">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741657095/wireframe_uploads_d95ehm.png" width="45%">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741657094/wireframe_files_n2ra6d.png" width="45%">
</p>

#### Dialysis Records
<p align="center">
  <img src="https://res.cloudinary.com/dzibrzlq9/image/upload/v1741657095/wireframe_record_tbnapa.png" width="45%">
  
</p>

### Database design

The Dialysis Connect database is designed to support a community-driven platform for dialysis patients. It facilitates event management, user-generated posts and comments, document uploads, and dialysis records tracking. This database follows a relational structure to ensure data consistency, integrity, and efficient querying.

The database comprises of 6 tables:
- Users Table (users) - This table stores user information and serves as the primary reference for other tables.
- Events Table (events) - This table stores event details, allowing users to track appointments and reminders.
- Posts Table (posts) - This table manages user-generated posts within the community section.
- Comments Table (comments) - This table stores comments on posts, facilitating discussions.
- Dialysis Records Table (dialysis_records) - This table stores user-submitted dialysis records to help track health data over time.
- Uploaded Files Table (uploaded_files) - This table allows users to upload and manage medical documents and images.

#### Relationships

- **Users & Events:** One-to-many (a user can have multiple events).

- **Users & Posts:** One-to-many (a user can create multiple posts).

- **Users & Comments:** One-to-many (a user can comment on multiple posts).

- **Users & Dialysis Records:** One-to-many (each user maintains multiple dialysis records).

- **Users & Uploaded Files:** One-to-many (users can upload multiple files).

- **Posts & Comments:** One-to-many (each post can have multiple comments).

#### Design considerations

- **Data Integrity:** Foreign key constraints ensure data consistency.

- **Scalability:** Optimized indexing and proper normalization support future growth.

- **Security:** User authentication should be handled securely to restrict data access.

- **Performance:** Time-based indexing on created_at fields optimizes querying.


![ERD](https://res.cloudinary.com/dzibrzlq9/image/upload/v1740884780/DialysisConnect_gauzuh.png)


The ERD (Entity Relationship Diagram) was designed on [dbdiagram.io](https://dbdiagram.io/d/DialysisConnect-67c39901263d6cf9a0e91d6d)

  
### Technology used

| Category       | Technology & Version                                           | Other Dependencies                |
| -------------- | -------------------------------------------------------------- | --------------------------------- |
| Backend        | Django 4.2.19 (Django==4.2.19)                                 |                                   |
| API            | Django REST Framework (djangorestframework==3.15.2)            | asgiref==3.8.1                    |
| Database       | PostgreSQL (psycopg2==2.9.10)                                  | dj-database-url==0.5.0            |
| Authentication | OAuth (oauthlib==3.2.2)                                        | django-environ==0.12.0            |
| Frontend       | JavaScript, JSON, HTML5, CSS3                                  | google-api-python-client==2.161.0 |
| Styling        | Bootstrap                                                      | google-auth-httplib2==0.2.0       |
| Media Storage  | Cloudinary (cloudinary==1.36.0, dj3-cloudinary-storage==0.0.6) | google-auth-oauthlib==1.2.1       |
| Static Files   | Whitenoise (whitenoise==6.9.0)                                 | googleapis-common-protos==1.67.0  |
| Server         | Gunicorn (gunicorn==20.1.0)                                    | httplib2==0.22.0                  |
| Image Handling | Cloudinary (cloudinary==1.36.0)                                | idna==3.10                        |
|                |                                                                | packaging==24.2                   |
|                |                                                                | proto-plus==1.26.0                |
|                |                                                                | protobuf==5.29.3                  |
|                |                                                                | psycopg2-binary==2.9.10           |
|                |                                                                | pyasn1==0.6.1                     |
|                |                                                                | pyasn1_modules==0.4.1             |
|                |                                                                | pyparsing==3.2.1                  |
|                |                                                                | pytz==2025.1                      |
|                |                                                                | requests==2.32.3                  |
|                |                                                                | requests-oauthlib==2.0.0          |
|                |                                                                | rsa==4.9                          |
|                |                                                                | setuptools==75.8.0                |
|                |                                                                | six==1.17.0                       |
|                |                                                                | sqlparse==0.5.3                   |
|                |                                                                | typing_extensions==4.12.2         |
|                |                                                                | tzdata==2025.1                    |
|                |                                                                | uritemplate==4.1.1                |
|                |                                                                | urllib3==1.26.20                  |


### Tools used

- Git: Used commands such as `git` `add` - `commit -m "message'` - `push`.
- VS code: Used as my IDE.
- Github: Used as the code hosting.
- [Favicon io](https://favicon.io/favicon-converter/): Used to generate the faveicon.
- [Balsamiq](https://balsamiq.com/wireframes/desktop/): Used to create the wireframes - desktop version.
- [Cloudinary](https://cloudinary.com/): Used to host all my images.
- [dbdiagraim.io](https://dbdiagram.io/home): Used to create the ERD.
- [cloudconvert](https://cloudconvert.com/mp4-to-gif): Used to convert video to gif

## Migration from Gitpod to VS code

I initially started my project using Gitpod but later needed to migrate to VS Code. During the migration process, I encountered several challenges that made it difficult to seamlessly transfer the project. As a result, I ultimately decided to set up a fresh environment in VS Code and manually copy my existing code from Gitpod to ensure a smooth transition.

## Fixed bugs



## Testing

For a detailed overview of both manual and automated testing processes, please refer to [TESTING.md](https://github.com/NontyD/dialysis_diary/blob/main/TESTING.md). It covers all testing scenarios and methodologies used in the project.

## Deployment

### Heroku

The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name ( for this project, the name is travellingplanner) and then choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars add the private API key information using key 'CRED' and into the value area copy the API key information added to the .json file.  Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9.  Choose the branch you want to build your app from
10. If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Find the repository you want to fork by either searching for it using the search bar or by directly navigating to its URL.
3. Once you're on the repository's main page, locate the "Fork" button in the upper-right corner of the page, usually next to the "Star" button.
4. Click on the "Fork" button.

#### How to Clone

To clone the repository:

* Click on the "Code" button in your forked repository.
* Copy the repository URL (HTTPS, SSH, or GitHub CLI).
* Open a terminal (or command prompt) on your computer.
* Run the following command: git clone <github.com/nontyd/dialysis_diary>



## Credits


[ChatGPT 4o](https://openai.com/chatgpt/) / [Codeium](https://codeium.com/) / [Stack Overflow](https://stackoverflow.com/) for adjustments and bug fixing aid.

The main idea for this project was obtained by the [Django Blog](https://www.youtube.com/watch?v=YH--VobIA8c) walkthrough project of the [Code Institute course](https://codeinstitute.net/global/).

### Media

Hero image used in the project was taken from [Freepik](https://www.freepik.com/).
Favicon was generated from [Design.com](https://www.design.com/logo-maker)