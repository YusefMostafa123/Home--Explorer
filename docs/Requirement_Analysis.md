# OverView  
Our goal with the Home Listing and Price Explorer project is to make a data driven application that will help users explore and analyze property listings for New York City. It is designed to function as a property search tool and a dashboard for visualizing trends. Our application will combine multiple public data sets so the user can not only see the basic information you would expect to see about a home listing like price, beds, baths, size but also have a deep understanding of the context and the surroundings of the home like nearby crime, school quality, and fire department coverage which will give users a richer understanding of the environment around each home.

Users will be able to look up homes, filter results based on things like price, area, number of bedrooms or bathrooms, and see analytics that summarize price distributions of homes. The main goal of the program is to give an intuitive and visually pleasing way to understand data about housing, letting users compare listings and make informed decisions. It will mix the functionality of a typical listing browser with functions, including searching and filtering, with a dashboard component, like displaying charts and averages.

There will be two main roles in our system: 
Program User: The buyer can utilize all the functionality talked about to compare homes. The user will also be able to list favorite listings.
Admin: Is responsible for maintaining the data in the system. Admins can load cleaned datasets into the database, refresh them when new versions are available, and control thresholds for analytics, for example, the ranges we use to check nearby crimes.

# Data Requirements  
Our program is built around several integrated tables. The housing table is central and main one, and the other datasets will enrich each listing with neighborhood indicators.

### Listings  
for each property we have our dataset contains:  
Id (unique listing identifier)  
Area (total square footage of the property)  
Bedrooms (number of bedrooms)  
Bathrooms (number of bathrooms)  
Floors (number of floors)  
YearBuilt (the year the home was constructed)  
Location (category of area (Downtown, Suburban, Urban, or Rural))  
Condition – (rating of the home’s overall condition (Excellent, Good, Fair, Poor))  
Garage – (indicates whether a garage is available (Yes/No))  
Price – (current market listing price in USD)  

### User (for favorites and reviews)  
UserId, Name, Email, PasswordHash  

### Favorites  
Represents a many to many relationship between users and listings.  
Each record stores (UserId, ListingId)  

### Reviews  
Each review belongs to a single user and a single listing.  
Attributes include (ReviewId, UserId, ListingId, Rating [1–5], Comment)  

This data structure will support the dashboard analytics (using numerical attributes like price, area, and year built) and  app interactions (using listings, users, favorites, and reviews))  

# Application Requirements  

### User:

### Agent

### Computed Behavior



