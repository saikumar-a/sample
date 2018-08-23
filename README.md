X, y = data[:, 0], data[:, 1] -- First column values in X and second column values are in y
When a graph is written in the form y = mx + c, m represents the gradient and c represents the y intercept.


JIRA
----
1. Gadget -- Filter Results
2. Open Issues -- resolution = Unresolved AND assignee = <Username> AND updatedDate > -30d ORDER BY updatedDate
3. Watched Issues -- key in watchedIssues() AND resolution = Unresolved AND status != Done AND (assignee != SAmmagar OR assignee is EMPTY) AND updatedDate > -30d ORDER BY updatedDate 


Bookmarklet
-----------
1. Single signon - http://username:password@google.com
2. imacros for chrome extension for forms automation
3. Bookmarklet -- javascript:function enterLogin(){a="myUserID";b="passwordinbase64";document.getElementById('wm_login-password').value=window.atob(b);document.getElementById('wm_login-username').value=a;document.getElementById('submit_login').click()}enterLogin();
4. Insert text to splunk textbox-- press spacebar after bookmarklet -- javascript:(function(a){a.value=a.value.slice(0,a.selectionStart)+"this is going to paste"+a.value.slice(a.selectionEnd);})(document.activeElement);

webmethods
-----------
1. You can test the flow services through soap ui using rest resource
POST method -- http://host:port/invoke/pub.math:addInts with json parameters
{
"num1" :"12",
"num2" :"14"
}
