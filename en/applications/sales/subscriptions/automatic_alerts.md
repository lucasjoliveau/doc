# Automatic alerts

Now that your subscriptions are up and running, you want to stay up-to-date
with your customers. Some automation would be appreciated since you would not
want to go through the list of all your subscribers to check how things are
going. This is what the _Automatic Alerts_ feature is for.

For example, when customers subscribe to your magazine, you would probably
want to send them an email to welcome them and express your gratitude. Or, if
the satisfaction rate of your customers drops below 50%, you would probably
want to schedule a call with them to understand the reasons for their
dissatisfaction.

With **Konvergo ERP Subscriptions** , you can set automatic emails, create a “Call”
task for one of your salespeople so that he/she can try to understand your
customer’s dissatisfaction, and finally, why not automatically send
satisfaction surveys so customers can evaluate your services? All of that is
now possible.

## Create a new automatic alert

The following example shows how to create a new automatic alert to send
satisfaction surveys to your customers, by email, after one month of
subscription. To do so, go to Subscriptions ‣ Configuration ‣ Alerts, and
create a new alert.

![New automatic alert in Konvergo ERP Subscriptions](../../../_images/create-a-new-
automatic-alert.png)

  1. On the _Apply on_ section, first give the alert a name. Then, you can choose to apply this alert on a subscription template, on a specific customer, or even on a specific product. If you want to add more specifications, you can also specify the value of your MRR, the change rate of your MRR over a certain period of time, the value of the satisfaction rate, and even the stage to which you want to apply this alert.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>In this example, the alert is applied to a specific product, and the stage goes from
<em>Undefined</em> to <em>In Progress</em>.</p>
</div>

  2. For the _Action_ section, specify the _Action_ and the _Trigger on_. If the _Trigger on_ is set to _Modification_ , the action is triggered every time there is a change or anything added to the subscription, and all the conditions on the _Apply on_ section are met. Now, if the _Trigger on_ is set to _Timed condition_ , it means that the action is triggered based on the type of _Trigger date_. After that, you can choose your _Action_. You have the choice between _Create next activity_ , _Set a tag on the subscription_ , _Set a stage on the subscription_ , _Mark as To Renew_ , _Send an email to the customer_ and _Send an SMS Text Message to the customer_.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>In the example above, the <em>Trigger on</em> is set to <em>Timed condition</em>, therefore, a
<em>Trigger date</em> and <em>Delay after trigger</em> need to be specified. And because the <em>Send an email
to the customer</em> action was adopted, an <em>Email template</em> can be chosen.</p>
</div> <div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Sending a SMS text message in Konvergo ERP requires In-App Purchase (IAP) credit or tokens. For more
information on <abbr title="In-App Purchase">IAP</abbr>, visit
<a href="../../essentials/in_app_purchase">In-app purchases (IAP)</a>. For more information on sending SMS messages,
visit <a href="../../marketing/sms_marketing/essentials/sms_essentials">SMS essentials</a>.</p>
</div>

As a result, this alert sends a rating survey after one month, to the
customers who have purchased that specific product. The survey appears in the
chatter of your respective subscription.

![Satisfaction survey in Konvergo ERP Subscriptions](../../../_images/rating-
satisfaction-survey.png)

## Modify an existing automatic alert

By default, Konvergo ERP suggests you an automatic alert called _Take action on less
satisfied clients_.

![Modify an existing automatic alert in Konvergo ERP
Subscriptions](../../../_images/modify-an-existing-automatic-alert.png)

This alert is applied to the _Rating Satisfaction_ of your customers, and the
action is triggered on _Timed condition_. If their satisfaction rate is lower
than 50%, a salesperson contacts the customer. This action is automatically
assigned to the salesperson who manages the subscription, and the due date is
5 days after the triggering of this action. This alert ensures that your
clients are happy and that you are taking actions if they are not. It helps to
keep your customer retention rates very high.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>By editing the alert, you can modify the <em>Apply on</em>, the <em>Action</em> and <em>Activity</em> sections, and
adapt them to your own needs.</p>
</div> <div class="alert alert-secondary">
<p class="alert-title">
See also</p><ul>
<li><p><a href="../subscriptions">Subscriptions</a></p></li>
<li><p><a href="plans">Subscription plans</a></p></li>
<li><p><a href="products">Subscription products</a></p></li>
<li><p><a href="../../essentials/in_app_purchase">In-app purchases (IAP)</a></p></li>
</ul>
</div>

