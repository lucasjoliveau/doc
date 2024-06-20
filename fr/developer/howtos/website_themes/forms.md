# Forms

Forms in Odoo are very powerful. They are directly integrated with other
applications and can be used for many different purposes.

In this chapter, you will discover how to:

  * Add a form in your custom theme.

  * Change the action of the form.

  * Stylize the form thanks to Bootstrap variables.

## Default form

To add a form to your page, you can simply copy and paste the code generated
by the Website Builder in your view.

It should look something like the following.

    
    
    <form action="/website/form/" method="post" enctype="multipart/form-data" class="o_mark_required" data-mark="*" data-pre-fill="true" data-success-mode="redirect" data-success-page="/contactus-thank-you" data-model_name="mail.mail">
         <div class="s_website_form_rows row s_col_no_bgcolor">
              <div class="form-group s_website_form_field col-12    s_website_form_dnone" data-name="Field">
                   <!-- form fields -->
               </div>
         </div>
    </form>
    

## Actions

There is a `data-model_name` in the form tag. It enables you to define
different actions for your form.

Send an email (this action is used by default).

    
    
    <form data-model_name="mail.mail">
    

Apply for a job.

    
    
    <form data-model_name="hr.applicant">
    

Create a customer.

    
    
    <form data-model_name="res.partner">
    

Create a ticket.

    
    
    <form data-model_name="helpdesk.ticket">
    

Create an opportunity.

    
    
    <form data-model_name="crm.lead">
    

Create a task.

    
    
    <form data-model_name="project.task">
    

## Success

You can also define what happens once the form is submitted thanks to the
`data-success-mode`.

Redirect the user to a page defined in the `data-success-page`.

    
    
    <form data-success-mode="redirect" data-success-page="/contactus-thank-you">
    

Show a message (on the same page).

    
    
    <form data-success-mode="message">
    

You can add your success message directly under the form tag. Always add the
`d-none` class to make sure that your success message is hidden if the form
hasn’t been submitted.

    
    
    <div class="s_website_form_end_message d-none">
         <div class="oe_structure">
              <section class="s_text_block pt64 pb64" data-snippet="s_text_block">
                   <div class="container">
                         <h2 class="text-center">This is a success!</h2>
                   </div>
              </section>
         </div>
    </div>
    

## Bootstrap variables

As you already know, the Website Builder creates content based on Bootstrap.
This is also true for forms. Below you can find a selection of Bootstrap
variables, or check out the [full list of
variables](https://github.com/twbs/bootstrap/blob/main/scss/_variables.scss).

`/website_airproof/static/src/scss/bootstrap_overridden.scss`

    
    
    $input-padding-y:                       $input-btn-padding-y !default;
    $input-padding-x:                       $input-btn-padding-x !default;
    
    $input-font-family:                     $input-btn-font-family !default;
    $input-font-size:                       $input-btn-font-size !default;
    $input-font-weight:                     $font-weight-base !default;
    $input-line-height:                     $input-btn-line-height !default;
    
    $input-color:                           $gray-700 !default;
    $input-border-color:                    $gray-400 !default;
    $input-border-width:                    $input-btn-border-width !default;
    $input-box-shadow:                      inset 0 1px 1px rgba($black, .075) !default;
    $input-border-radius:                   $border-radius !default;
    
    $input-focus-bg:                        $input-bg !default;
    $input-focus-border-color:              lighten($component-active-bg, 25%) !default;
    $input-focus-color:                     $input-color !default;
    $input-focus-width:                     $input-btn-focus-width !default;
    $input-focus-box-shadow:                $input-btn-focus-box-shadow !default;
    
