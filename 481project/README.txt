To populate project, navigate to localhost:port/drinks/populate where port is the number assigned to the port when you add the project to GAE. It will take about 7-10 minutes,
maybe longer depending on the computer, to completely populate the database, please be patient.

An important note, the home page is at localhost:port/drinks/ if you just go to localhost:port/ you will see an error message

Before using this site be sure to delete all cookies that may still exist from using other projects as they may negatively impact the performance of the site.

Once done uploading you should receive a message and a link to the home page. 

That link will take you to localhost:port/drinks/ from there:
you can go to the create user page by clicking the associated button
you can log in to an existing user
you can select a drink type from the dropdown menu to view a list of the drinks of that type, and then go to a drinks detail page
you can click the link to the search function

The search function allows you to select the ingredients you own from a list of all ingredients in all of the drinks in the database
and the website will generate a list of drinks you can make and a recommendation as to what you should buy next to increase the number
of drinks you can make by the greatest amount. The search function does take about 30 seconds to a minute to process, so don't click the button more than once or it will be forced to start over.

If you are logged in, which can only be done from the main drink library page or from a specific drink's page, 
the system will remember what ingredients you searched for and will have those selected the next time you go to search.
the system will also keep track of the last drink you visited during your current session and display a link to that drink
Also if you have completed a search there will be a button to take you back to the search results, be patient with the results page, it is a little slow.

If logged in when looking at a drink's detailed page, you can add that drink to your drink list, which can be accessed through the link at the top for easier reference later.

If for some reason you need to empty the database, copy the contents of empty.txt into the Interactive Console in the SDK Console and click execute.
This will take several minutes to process as well, and should only be done when necessary.

If any problems arise during testing please contact the developer at Philip.Sauvey@gmail.com