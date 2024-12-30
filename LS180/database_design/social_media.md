# Social Media Network Database
Database design practice for LS181 interview

## Scenario:

- You're tasked with designing a database for a new social media platform. The platform needs to support user profiles, friend connections, posts, comments, and likes. How would you model these relationships in your database design? Use Crow's foot notation to illustrate the cardinality and modality of these relationships. Explain how your design supports or prevents certain anomalies.

### Design

First we need to identify the entities that will be present in our database.

1. Users
2. Posts

Identify relationships among the entities on a conceptual level based on the requirements we need to support

- Users
  - Have one user profile
  - Have many friend connections
  - Have many posts
  - Have many comments
  - Have many likes
- Posts
  - Have one original user
  - Do not have friend connections
  - Have many comments
  - Have many likes
- Comment
  - Have one original user
  - Do not have friend connections
  - Belong to a post or another comment under that post
  - Comments do not have likes
- Like
  - Have one original user who performed the like
  - Belong to one post
  - Do not have friend connections
  - Do not relate to comments

- Design Choices
  - To not implement comments having likes to decrease the initial complexity of the likes system

- ERD w/ crow's foot notation from LucidChart

- How Constraints affect the database functionality
  - Primary keys: ensure unique identification of rows in each table
  - Foreign Keys: Enforce data integrity and prevent orphaned rows (through `ON DELETE` clauses)
  - Check constraints: validate pairs and data types
  - Unique constraints: Maintain a 1:1 relationship or a 1:M relationship between tables
  - Not Null: prevents incomplete data from being filled when used properly
  

