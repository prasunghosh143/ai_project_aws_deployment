# MINOR PROJECT DOCUMENTATION

## Kitto AI
### AI-Powered Content Generation Platform

| Field | Details |
|---|---|
| Project Name | Kitto AI — AI-Powered Content Generation Platform |
| Project Type | Minor Project (Web Application) |
| Technology | Python, Django 5.1, HTML5, CSS3, JavaScript, SQLite/PostgreSQL, Google GenAI |
| Academic Year | 2025–26 |
| Department | Computer Science / Information Technology |
| Project Guide | Not specified in repository |
| Team Members | Not specified in repository |

## 1. Project Definition

Kitto AI is a web-based AI content generation platform designed to generate paragraph-style content, summaries, stories, and other structured writing from a user-provided topic, subject, or prompt. The application is built with Django and serves as a practical academic minor project that demonstrates full-stack web development, authentication, database persistence, cloud-ready configuration, and AI-assisted content generation.

The core purpose of the system is simple: the user enters a topic, chooses a writing intent, and receives a structured paragraph or short-form response that can be used for study material, assignment support, content drafting, or general writing assistance. The application is not a generic chatbot. It is purpose-built for paragraph generation and related writing tasks, with a focus on producing clean, readable, and context-aware text.

The project includes a landing page, login and signup flows, a generation interface, a dashboard for history review, public feedback collection, a health-check endpoint, and sitemap support. It stores generated content in the database so that users can revisit past results. When the remote AI model is unavailable, the application falls back to a local deterministic generation path so the user still receives useful output.

From an academic perspective, Kitto AI demonstrates the following ideas:

1. Form handling and server-side validation in Django.
2. Authentication and session management.
3. Database modeling and content persistence.
4. Third-party AI integration through the Google GenAI SDK.
5. Graceful fallback behavior when an external service fails.
6. Streaming output using Server-Sent Events.
7. Deployment readiness using environment-based configuration.

The project is therefore suitable as a minor project documentation example for a web application centered on AI-assisted writing.

## 2. Features

Kitto AI provides the following features to help users generate and manage AI-created content efficiently.

### 2.1 Topic-Based Paragraph Generation

The system allows a user to enter a topic or prompt and receive generated writing based on that input. The prompt can be as short as a keyword or as detailed as a writing instruction. The output is intended to be natural language text that can function as a paragraph, overview, explanation, short story, or summary depending on the prompt intent.

The generation flow is designed to be flexible. For example, a user may ask for a paragraph about artificial intelligence, a story about friendship, or a summary of a concept. The AI model interprets the request and returns content directly, without unnecessary conversational filler.

### 2.2 AI-Backed Content Creation

The application connects to Google GenAI using the `google-genai` client library. When the `MAIN_API_KEY` environment variable is present, the system sends the prompt to the configured Gemini model and receives a generated response. The model is configurable through `GEMINI_MODEL`, with `gemini-2.0-flash` as the default in the repository settings.

This makes the application capable of producing more sophisticated and polished writing than a static template-based generator. It also makes the project relevant to real-world AI integration patterns.

### 2.3 Local Fallback Content Generator

If the external API is unavailable, the application does not stop working. Instead, it generates fallback content locally based on the prompt type. The fallback path recognizes common intent patterns such as:

1. Summary requests.
2. Story requests.
3. General overview requests.

This ensures the application remains usable even if the external model cannot be reached, the key is missing, or a request fails unexpectedly.

### 2.4 Streaming Response Support

The application includes a Server-Sent Events endpoint that streams generated text progressively. This improves user experience because the content begins appearing before the entire response is complete. The endpoint sends metadata, chunks the response into sentence-like segments, and then sends a completion event.

This feature is particularly useful for larger responses or slower model calls, since the interface can begin displaying content immediately.

### 2.5 Authentication System

The project supports user registration, login, and logout using Django’s built-in authentication framework with a custom signup form. New users must provide a unique email address and agree to the terms and conditions before creating an account.

This allows the application to distinguish registered users from anonymous visitors and redirect authenticated users to the dashboard.

### 2.6 Generated Content History

Every successful generation is stored in the database as a `GeneratedContent` record. The dashboard shows recent entries so the user can review past prompts and outputs without generating them again.

This history feature adds practical value and makes the project feel like a usable writing tool rather than a one-time demo page.

### 2.7 Public Feedback Collection

Anonymous users can submit feedback from the landing page. This gives the project a simple public-facing contact mechanism and demonstrates how to save user-provided text to the database.

### 2.8 Health Check Endpoint

The application includes a health endpoint that verifies database connectivity. This is useful for hosting environments that need to determine whether the app is healthy and responsive.

### 2.9 Sitemap Support

The project exposes a sitemap XML file that lists the important public views. This is useful for search engine indexing and for showing that the site includes structured routing support.

### 2.10 Deployment-Ready Configuration

The settings are designed to support both local and production use. The project can run with SQLite for development and PostgreSQL when `DATABASE_URL` is configured. It also uses WhiteNoise for static file serving and supports secure production behavior such as SSL redirect, secure cookies, and trusted CSRF origins.

## 3. Requirements

### 3.1 Functional Requirements

The following table lists the major functional requirements of Kitto AI.

| FR# | Requirement | Description |
|---|---|---|
| FR01 | View Landing Page | System shall allow anonymous users to open the main landing page |
| FR02 | Submit Feedback | System shall allow users to submit feedback from the landing page |
| FR03 | Sign Up | System shall allow new users to create an account using username, email, and password |
| FR04 | Validate Email | System shall reject signup attempts using duplicate email addresses |
| FR05 | Accept Terms | System shall require acceptance of terms and conditions before registration |
| FR06 | Log In | System shall allow registered users to log in through a custom login page |
| FR07 | Log Out | System shall allow authenticated users to log out |
| FR08 | Generate Paragraph | System shall generate content from a user-supplied topic or prompt |
| FR09 | Calculate Word Count | System shall calculate and store the word count of generated content |
| FR10 | Save Generated Content | System shall store generated outputs in the database |
| FR11 | Show Dashboard | System shall display recent generation history to the user |
| FR12 | Stream Output | System shall support streaming generation through Server-Sent Events |
| FR13 | Fallback Mode | System shall create local fallback content if the remote AI path fails |
| FR14 | Health Check | System shall expose a health endpoint to verify database connectivity |
| FR15 | Sitemap | System shall expose a sitemap XML endpoint |

### 3.2 Non-Functional Requirements

| Category | Requirement |
|---|---|
| Performance | The system should return generation results as quickly as the AI service permits, and streaming should begin output as early as possible |
| Usability | The interface should be simple, clean, and easy to use for students and general users |
| Reliability | The app should continue to work through fallback content generation if the external AI service fails |
| Portability | The application should run locally with SQLite and in deployment with PostgreSQL |
| Security | The system should support secure authentication, CSRF protection, and production SSL behavior |
| Maintainability | The codebase should remain organized by Django app structure and environment-based configuration |
| Scalability | The architecture should allow future expansion into more advanced writing tools or multi-user content systems |
| Accessibility | The templates should remain responsive and usable on desktop and mobile screens |

### 3.3 Hardware and Software Requirements

| Component | Specification |
|---|---|
| Operating System | Windows 10+, Windows 11, macOS, Linux |
| Web Browser | Google Chrome, Mozilla Firefox, Microsoft Edge, Safari |
| Processor | Any modern processor capable of running a web server and browser |
| RAM | Minimum 1 GB recommended for development; production depends on hosting platform |
| Storage | Small project footprint, mostly Python source files, templates, and SQLite database for local use |
| Internet | Required for AI API access; not strictly required when fallback content is used locally |
| Development Tools | VS Code, PyCharm, or any text editor and terminal capable of running Django |

## 4. Coding

Kitto AI is built using Django on the backend and HTML, CSS, and JavaScript on the frontend. The application follows a typical web application architecture with templates, static assets, models, forms, URLs, and views separated into logical parts.

### 4.1 Project Structure

The repository is organized into the following main components:

| File / Folder | Description |
|---|---|
| `manage.py` | Django command-line entry point |
| `ai_project/` | Project configuration package containing settings, root URLs, WSGI, and ASGI files |
| `paragraph_generator/` | Main application package containing models, views, forms, URLs, tests, and helpers |
| `paragraph_generator/templates/` | Django HTML templates for auth pages, landing page, generation page, dashboard, and navigation |
| `paragraph_generator/static/` | Static assets such as CSS and JavaScript |
| `db.sqlite3` | Local development database |
| `requirements.txt` | Python package dependencies |
| `Procfile` | Deployment process configuration |
| `railway.toml` | Railway deployment metadata |
| `nixpacks.toml` | Build configuration for Nixpacks-based deployment |

### 4.2 HTML and Template Structure

The application uses server-rendered Django templates. The following pages are included:

1. Landing page template for the public home screen.
2. Login template for user authentication.
3. Signup template for account creation.
4. Generate template for prompt submission and content display.
5. Dashboard template for recent generation history.
6. Shared navigation template included across pages.

The templates are designed to keep the interface simple while still supporting the project’s core features. The generation page is the primary working screen, while the landing page introduces the application and collects feedback.

### 4.3 CSS Highlights

The project includes CSS files for the landing page, dashboard, generation page, login, and signup pages. The styles are organized within the static directory and can be extended as needed.

Important styling concepts used in the project include:

1. Responsive layout for desktop and mobile use.
2. Card-based visual presentation for content sections.
3. Button and form styling for clear user interaction.
4. Visual separation of history, input, and output areas.
5. Simple design patterns suited for an academic web project.

The CSS is not framework-dependent, which keeps the project easy to understand and modify.

### 4.4 Core JavaScript and Frontend Logic

The repository includes a JavaScript file for Tailwind CSS support, but the main application logic is handled on the Django side. Frontend scripting can be used for asynchronous generation requests, live rendering of streamed content, and dynamic updates on the page.

Key client-side behaviors may include:

1. Submitting generation requests without full page reload.
2. Displaying streamed content as it arrives.
3. Presenting success and error messages.
4. Updating the UI when a generation completes.

### 4.5 Backend Views and Application Logic

The primary logic is implemented in `paragraph_generator/views.py`. The important views are:

| View | What It Does |
|---|---|
| `index()` | Shows the landing page, redirects authenticated users to the dashboard, and accepts public feedback submissions |
| `signup_view()` | Handles user registration and login after successful signup |
| `generate_paragraph_index()` | Accepts prompt input, calls the Gemini API, and saves generated content |
| `stream_generate()` | Streams generated content progressively using Server-Sent Events |
| `dashboard()` | Displays recent generated content entries |
| `user_logout()` | Logs the user out and redirects to the landing page |
| `check_reset_daily_limit()` | Supports daily API usage tracking, though the current generation flow does not enforce a visible limit |

### 4.6 Content Generation Code Path

The generation process works as follows:

1. The user submits a topic or prompt.
2. The server validates that the topic is not empty.
3. The system builds a prompt for the AI model.
4. If a `MAIN_API_KEY` is available, the application creates a Gemini client and requests content.
5. The result is parsed from the API response.
6. The system calculates the word count.
7. The content is stored in the database.
8. A JSON response is returned to the browser.

If the API call fails, the view falls back to a local generator that creates content based on whether the prompt looks like a summary request, a story request, or a general paragraph request.

### 4.7 Streaming Generation Code Path

The streaming endpoint is designed to improve perceived speed and user experience. Instead of waiting for the full response, it yields incremental chunks to the browser.

The flow includes:

1. Opening an SSE connection.
2. Sending metadata about whether the response is fallback-based.
3. Checking for an API key.
4. Generating fallback content when necessary.
5. Splitting content into sentence-like chunks.
6. Yielding each chunk as SSE data.
7. Emitting a final done event.
8. Saving the result in the database.

This code path is a useful demonstration of asynchronous-style user experience in a Django application.

### 4.8 Input Validation

Input validation is implemented in the signup form and generation flow. The current validations include:

1. Topic field cannot be blank.
2. Email must be unique during signup.
3. Terms must be accepted before account creation.
4. Password and password confirmation must satisfy Django’s built-in validation rules.

Additional validation such as rate limiting or content moderation can be added in future versions.

### 4.9 Data Model

The application stores information using Django models. The current models are:

| Model | Purpose |
|---|---|
| `GeneratedContent` | Stores prompts, generated text, word count, topic, and timestamp |
| `UserApiUsage` | Stores per-user usage tracking fields |
| `Feedback` | Stores user-submitted feedback from the landing page |

Example generated content object:

```python
GeneratedContent.objects.create(
    prompt=prompt,
    content=content,
    word_count=word_count,
    topic=topic[:200],
)
```

Example signup form validation logic:

```python
def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("A user with this email already exists.")
    return email
```

### 4.10 Authentication and Session Handling

Authentication is handled through Django’s standard user model. A custom login view is used to connect the login screen to the templates in the repository. After signup, the user is automatically logged in and redirected to the dashboard. Logout returns the user to the landing page.

### 4.11 Route Structure

The current URL configuration includes the following routes:

| Route | Purpose |
|---|---|
| `/` | Landing page and feedback submission |
| `/login/` | Login page |
| `/signup/` | Signup page |
| `/logout/` | Logout action |
| `/dashboard/` | Recent generation history |
| `/generate/` | Generation page and synchronous generation endpoint |
| `/stream-generate/` | Streaming generation endpoint |
| `/health/` | Health check |
| `/sitemap.xml` | Sitemap |
| `/ggfhfhchv/` | Django admin path |

## 5. Future Scope

Kitto AI is already functional, but several enhancements can improve it further.

### 5.1 Data Persistence Enhancements

At present, generated content is stored in the database, but the application could be expanded with additional persistence features such as:

1. Search and filter for old generations.
2. Pagination in the dashboard.
3. Export of generated content to text or PDF.
4. User-specific libraries of saved paragraphs.

### 5.2 Advanced Writing Modes

The current system is focused on paragraph writing, but future versions may support more detailed writing modes:

1. Essay generation.
2. Summary generation.
3. Story writing.
4. Formal explanation mode.
5. Simple language mode for school-level content.
6. Tone selection such as academic, professional, creative, or conversational.

### 5.3 Prompt Improvement Tools

The user experience can be improved with smarter prompt guidance:

1. Prompt suggestions and examples.
2. Word count selection.
3. Topic category selection.
4. Writing style presets.
5. Length controls for short, medium, and long paragraphs.

### 5.4 Usage Limiting and Quota Tracking

The repository already includes a `UserApiUsage` model and a helper for resetting daily usage. Future versions can build on this to implement:

1. Daily generation limits.
2. Usage alerts for heavy users.
3. Plan-based access control.
4. Admin visibility into usage trends.

### 5.5 Better Dashboard and Review Tools

The dashboard could evolve into a richer workspace where users can:

1. View all previous generations.
2. Re-run an old prompt.
3. Edit and save a generation.
4. Copy generated content to clipboard.
5. Mark favorites or archive old results.

### 5.6 Cloud and Multi-Device Support

Future versions could support synchronized user data across devices using a cloud database and user profiles. This would be helpful if the project is later turned into a full academic tool or deployed as a service for multiple users.

### 5.7 Notification and Reminder System

Potential future notifications include:

1. Generation completed alerts.
2. Daily writing reminders.
3. Prompt optimization hints.
4. Account verification reminders.

### 5.8 Mobile-Friendly Improvements

The current templates can be extended into a more polished mobile-first experience with improved spacing, collapsible panels, and touch-friendly controls.

### 5.9 Testing and Quality Assurance

The current test module is minimal. Future releases should add tests for:

1. Signup validation.
2. Login/logout flow.
3. Content generation success and fallback behavior.
4. Streaming response format.
5. Health endpoint behavior.
6. Dashboard access.

## 6. Summary of Future Enhancements

| # | Feature | Technology / Approach | Priority |
|---|---|---|---|
| 1 | Prompt History Search | Django ORM + query filters | High |
| 2 | Download Generated Text | File response / export helper | High |
| 3 | Writing Style Selector | Form controls + prompt engineering | High |
| 4 | Daily Usage Limits | Existing `UserApiUsage` model | Medium |
| 5 | Dashboard Pagination | Django pagination | Medium |
| 6 | Tone / Length Controls | Frontend form fields | Medium |
| 7 | Multi-Device Sync | PostgreSQL / cloud user data | Low |
| 8 | Notifications | Email or browser notifications | Low |

## 7. Conclusion

Kitto AI is a minor project web application that demonstrates how Django can be used to build an AI-powered content generation platform. It combines user authentication, AI text generation, streaming output, database persistence, feedback handling, and deployment-ready settings in one structured system.

The application is useful as both an academic submission and a real software prototype because it solves a focused problem: helping users generate paragraph-style content quickly and reliably. The fallback generator ensures the project remains practical even when external AI services are unavailable, and the stored history makes the system useful beyond a single request-response cycle.

This document should be kept aligned with the codebase as the project evolves so that the requirements, features, and implementation details remain accurate.