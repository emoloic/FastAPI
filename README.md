1- Automatic docs
1.1- Swagger UI
Whenever you create an api, how are going to check that. Generally we use a tool such as Postman but that is not good thing. By default, FastAPI provides us a Swagger UI (very nice UI that you can simply check what are the routes we are created, our API endpoints)
1.2- Redoc
FastAPI provides another ReDoc UI. This is the same but has a minimal design for the documentation.
2- Modern Framework
Since it is a modern framework, it also uses a modern features of Python. It uses Python 3.6 and more with type using Pydantic.
3- Based on open standards
JSON schema: By default, it returns JSON which every modern API needs to communicate with other things.
Open API is a linux foundation, it defines how you create your API. It helps us create our API in a recommended way.
4- VsCode|PyCharm Editor support
Fast API has the auto completion in VSCode and PyCharm. This feature allows us to write APIs very fast.
5- Security and Authentication
HTTP Basic, OAuth2(also with JWT tokens), API keys in (headers, Query parameters, Cookies).
6- Dependency injection, Unlimited plug-ins, Testing
7- Starlette Features
Starlette is another framework of Python. Starlette provides:
- WebSocket support
- GraphQL support
- In-process background tasks
- Startup and shutdown events
- Test client built on requests
- CORS, GZip, Static Files, Streaming responses
- Session and Cookie support
8- Other Supports (SQL databases, NoSQL databases, GraphQL)

This project covers the following concepts:
1- Basic Concepts
- Path Parameters
- API Docs
- Query parameters
- Request body
2- Intermediate Concepts
- Pydantic Schemas
- SQLAlchamey database connection (used to connect to the database)
- Models and table (create a model and use that model to create a table in the database)
3- Database Tasks
- Store blog to database
- Get blogs from database
- Delete
- Update
4- Responses
- Handling Exceptions
- Return response
- Define response model (so that we can only show certain fields which we only want) For example, if we don't want to show the password of the user, how we can restrict that.
5- User and Password
- Create user
- Hash user password (using the bcrypt algorithm)
- Show single user
- Define docs tags
6- Relationship
Since we are using SQLAlchamey, we will:
- Define User to Blog relationship
- Define Blog to User relationship
7- Refactoring
- API Router
- API Router with Parameter
8- Authentication using JWT
JWT stands for JSON Web Token, we will:
- Create Login route
- Login and verify password (using the hash algorithm)
- Return JWT access token
- Routes behind authentication
9- Deploy FastAPI
- Usng Deta.sh website to deploy.

Let's now see what will be the final product we 

1- FastAPI Swagger UI
You can see we have all the Blogs related routes behing the authentication.
2- FastAPI ReDoc