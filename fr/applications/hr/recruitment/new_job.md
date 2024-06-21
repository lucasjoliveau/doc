# Postes

Dans le tableau de bord Recrutement par défaut, tous les postes sont affichés,
indépendamment de leur statut. Les postes actuellement publiés avec des
candidats actifs sont affichés, ainsi que les postes qui ont été créés, mais
qui n’ont pas encore été publiés.

Chaque poste est affiché dans une carte kanban individuelle. Si le poste est
actif et les candidats peuvent postuler, une bannière **Publié** apparaît dans
le coin supérieur droit de la carte.

View submitted applications by clicking anywhere on a job position card.

![Tableau de bord principal du recrutement affichant tous les postes à
pourvoir.](../../../_images/jobs.png)

## Créer un nouveau poste

Create a new job position from the main Recruitment dashboard by clicking the
**New** button in the top-left corner.

Une fenêtre contextuelle **Créer un poste** s’affiche alors. Saisissez-y le
nom de la fonction (tel que `Directeur des ventes`, `Ingénieur mécanique`,
etc.). Lorsque vous avez terminé, cliquez sur le bouton **Créer** pour
enregistrer l’entrée ou sur le bouton **Ignorer** pour la supprimer.

![Créez un nouveau poste.](../../../_images/job-title.png)

Once the job position has been created, it will appear as a card in the kanban
view on the main **Recruitment** dashboard.

### Modifier un nouveau poste

After the job position is created, it’s time to enter the details for the
position. Click on the **⋮ (three dots)** icon in the upper-right corner of
the relevant card to reveal several options, and then click **Configuration**
to edit the details.

![Modifiez la carte du poste.](../../../_images/edit-job.png)

Enter the job description in the **Job Summary** tab. This information is what
is visible to potential applicants when searching for available jobs.

#### Recrutement

Toutes les informations de base concernant le poste à pourvoir sont
répertoriées sous l’onglet **Recrutement**. Aucun champ n’est obligatoire,
mais il est conseillé de fournir au moins quelques détails, tels que la
localisation du poste.

Les champs peuvent être remplis comme suit :

  * **Department** : select the relevant department for the job position.

  * **Job Location** : select the physical address for the job.

  * **Employment Type** : select what type of position the job is, such as **Full-Time** , **Part-Time** , etc.

  * **Company** : select the company the job is for.

  * **Target** : enter the number of employees to be hired for this position.

  * **Is Published** : activate this option to publish the job online.

  * **Website** : select the website where the job will be published.

  * **Recruiter** : select the person who will be doing the recruiting for this role.

  * **Interviewers** : select who should perform the interview(s). Multiple people can be selected.

  * **Interview Form** : select an Interview form that applicants will fill out prior to their interview.

  * **Contract Template** : select a contract template that will be used when offering the job to a candidate.

  * **Process Details** section: this section contains information that is displayed online for the job position. This informs the applicants of the timeline and steps for the recruitment process, so they know when to expect a reply.

    * **Time to Answer** : enter the number of days before the applicant is contacted.

    * **Process** : enter the various stages the candidate will go through during the recruitment process.

    * **Days to get an Offer** : enter the number of days before the applicant should expect an offer after the recruitment process has ended.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The <b>Process Details</b> section is a text field. All answers are typed in rather than
selected from a drop-down menu. The text is displayed on the website exactly as it appears in
this tab.</p>
</div> ![Saisissez les détails de la fonction dans l'onglet
recrutement.](../../../_images/recruitment-tab.png)

### Créer un formulaire d’entretien

An _Interview Form_ is used to determine if a candidate is a good fit for a
job position. Interview forms can be as specific or general as desired, and
can take the form of a certification, an exam, or a general questionnaire.
Interview forms are determined by the recruitment team.

All interview forms must be created, there are no pre-configured forms in
Konvergo ERP. To create an interview form, start from the recruitment tab of the **Job
Position** form. In the **Interview Form** field, enter a name for the new
interview form. As the name is typed, several options populate beneath the
entry, **Create (interview form name)** , **View all** , and **Create and
edit…**. Click **Create and edit…**. and a **Create Interview Form** pop-up
window appears.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>The option <b>View all</b> only appears if there are any interview forms already created.
If no interview forms exist, the only options available are <b>Create (interview form
name)</b>, and <b>Create and edit…</b>.</p>
</div>

First, enter a name for the form in the **Name** field. This should be
indicative of when the form should be used. For example, is the form specific
to a job position, or is it a general form that can be used for all
recruitment scenarios?

Next, select what kind of interview form is being created. The default is
**Custom** , which is pre-selected. The various options are **Survey** ,
**Live session** , **Assessment** , **Custom** , and **Appraisal**.

Then select the person responsible for the form from the drop-down menu for
the **Responsible** field.

If desired, an image can be added to the interview form. Mouse over the camera
icon on the far right and a **✏️ (pencil)** icon appears. Click the **✏️
(pencil)** icon and a file explorer window appears. Navigate to the desired
image file, then click **Open** to select it.

![The top portion of the new interview form with everything filled out and
selected.](../../../_images/create-interview-form.png)

#### Questions

In the **Questions** tab, click on **Add a section** to add a section to the
form. A line appears, and a section heading can be entered. When complete,
click off the line, or press enter to lock in the new section on the form.

Next, click **Add a question** to add a question to the section. A **Create
Sections and Questions** pop-up window appears where the question details are
entered. Type out the question in the top line.

There are several **Question Types** to choose from:

  * **Choix multiple : une seule réponse** : un choix multiple qui permet au candidat de ne sélectionner qu’une seule réponse

  * **Choix multiples : plusieurs réponses autorisées** : un choix multiple qui permet au candidat de sélectionner plusieurs réponses

  * **Zone de texte à lignes multiples** : permet au candidat de saisir plusieurs lignes de texte

  * **Zone de texte à ligne unique** : restreint le candidat à une seule ligne de texte

  * **Valeur numérique** : ne permet de saisir qu’un seul chiffre

  * **Date** : un module calendrier s’ouvre permettant de sélectionner une date

  * **Datetime** : a calendar module and a clock icon is presented to select a date and time

  * **Matrice** : un tableau personnalisable qui permet au candidat de choisir une réponse pour chaque ligne

After selecting a question type, a sample question appears in gray. This
represents how the question will be displayed to applicants.

![Ajoutez une nouvelle question au formulaire
d'entretien.](../../../_images/questions.png)

Vous pouvez réorganiser les questions et les sections. Déplacez-les en
cliquant sur les en-têtes de section ou lignes de question individuelles et en
les déplaçant à l’emplacement souhaité.

Les sections sont indiquées par un fond gris, tandis que les questions ont un
fond blanc.

![Un exemple de catégories et de questions pour un
candidat.](../../../_images/questions-matrix.png)

##### Réponses

If **Multiple choice: only one answer** , **Multiple choice: multiple answers
allowed** , **Single Line Text Box** , or **Matrix** is selected for the
**Question Type** , an **Answers** tab appears beneath the question. If
another question type is selected, the **Answers** tab remains hidden from
view.

Multiple choiceSingle Line Text BoxMatrix

For both the **Multiple choice: only one answer** and **Multiple choice:
multiple answers allowed** question type, the answers are populated in the
same way.

First, in the **Answers** tab, click **Add a line**. A line appears, and an
answer can be entered. After typing in the answer, click off the line, or
press enter to lock in the new answer on the form and have another answer line
appear.

If desired, an image can be attached to the answer. Click on a line to select
it, and an **Upload your file** button appears on the right side. Click the
**Upload your file** button and a file explorer window appears. Navigate to
the image file, select it, then click **Open** to select it.

Repeat this for all the answers to be added for the multiple choice question.
The answers can be rearranged in any order. To move an answer, click on the
six small squares on the far left of each answer line, and drag the answer to
the desired position. The order the answers appear in the form is the order
the answers will appear online.

To delete a line, click on the **🗑️ (trash can)** icon on the far right side
of the answer line.

![Answers to a multiple choice question, where each line has a different
answer listed.](../../../_images/multi-answers.png)

If the **Single Line Text Box** question type is selected, only two checkboxes
appear in the **Answers** tab:

  * **Input must be an email** : activate this option if the answer must be in the format of an email address.

    * **Save as user email?** : this option appears if **Input must be an email** is selected. This saves the email entered on the form as the user’s email, and will be used anytime Konvergo ERP contacts the user via email.

  * **Save as user nickname?** : activate this option to populate the answer as the user’s nickname. This is stored and used anywhere Konvergo ERP uses a nickname.

![The three possible checkboxes that can appear if a single line of text is
selected for the question type.](../../../_images/single-line.png)

Sometimes, a question is asked that does not fit a standard answer format, and
is best suited for a matrix. For example, asking an applicant what is their
availability to work compared to the various shifts is a perfect question for
a matrix format. In this example, an applicant can click on all the shifts
they are available to work.

For a **Matrix** question type, there are two sets of data that need to be
input. The rows and columns must both be configured. The columns are
represented by the **Choices** section, while the rows are configured in the
**Rows** section.

The method for populating both sections is the same. In the **Answers** tab,
click **Add a line** in either the **Choices** or **Row** section. A line
appears, and an answer can be entered. After typing in the answer, click off
the line, or press enter to lock in the new answer on the form and have
another answer line appear. Repeat this for all answers for both the
**Choices** and **Rows** sections.

![../../../_images/matrix.png](../../../_images/matrix.png)

This is an example matrix that asks an applicant what shifts they are
available to work on Saturdays and Sundays, either morning, afternoon, or
evening.

##### Description

Enter any information that may be helpful to an applicant. This description
will appear for this specific question only, and therefore should be question-
specific and not generalized.

##### Options

To view the options that are available to set for a question, click on the
**Options** tab. The **Layout** , **Constraints** , and **Live Sessions**
sections are universal for all **Question Types** , while the **Answers** tab
is specific to the **Question Type** selected, and changes based on the
selection.

###### Réponses

  * **Multiple choice: only one answer** and **Multiple choice: multiple answers allowed** : a **Show Comments Field** option appears. Activate the option to allow the applicant to answer the question by typing in an answer (or comment). A **Comment Message** and **Comment is an answer** field appear if activated. Enter the text to appear in the **Comment Message** field. This should be helpful to the applicant, such as `If other, please specify`. Last, if the comment should be logged as the applicant’s answer, activate the box.

  * **Multiple Lines Text Box** : a **Placeholder** field appears. Enter any text that should appear with the question to help clarify how the applicant should answer.

  * **Single Line Text Box** and **Numerical Value** : a **Validate entry** option appears. Activate this option if what the applicant enters must be a numerical value, _and_ needs to be verified. The answer can _only_ be verified if it is a numerical entry. When activated, several other options appear. Enter the values for the **Min/Max Limits** in the two fields. Next, enter the text that appears when the answer given does not fit within the designated minimum and maximum parameters. Last, enter any text in the **Placeholder** field to provide any additional information or directions to assist the applicant.

  * **Date** and **Datetime** : a **Validate entry** option appears. Activate this option if the applicant’s answer needs to be verified. When activated, several other options appear. Enter the date ranges for the **Min/Max Limits** in the two fields. Click on a field, either the **minimum** or **maximum** , and a calendar appears. Select the dates for the corresponding fields. Next, enter the text that appears when the answer given does not fit within the designated minimum and maximum dates. Last, enter any text in the **Placeholder** field to provide any additional information or directions to assist the applicant.

  * **Matrix** : the first option that appears is **Matrix Type**. Select either **One choice per row** or **Multiple choices per row** using the drop-down menu. The next option is **Show Comments Field**. Activate the option if there should be a comment displayed to the applicant. If activated, a **Comment Message** and **Comment is an answer** field appear. Enter the text to appear in the **Comment Message** field. This should be an instruction helpful to the applicant, such as `If other, please specify`. Last, if the comment should be logged as the applicant’s answer, activate the box.

###### Contraintes

If the question is required to be answered by the applicant, activate the box
next to **Mandatory Answer**. An **Error message** field appears, with some
example text in gray (_This question requires an answer_). Enter the message
that should appear if the applicant attempts to move on to the next question
without answering this required one. The text should explain that the question
must be answered.

###### Agencement

If the question should only appear if a previous question is answered in a
specific way, activate the **Conditional Display** option. A new **Triggering
Question** field appears. Using the drop-down menu, select the previous
question this new question is linked to. Once a previous question is selected,
a **Triggering Answer** field appears. Select the answer that must be selected
in order for the new question to appear.

<div class="alert alert-success">
<p class="alert-title">
Example</p><p>To further illustrate a triggering question, the following is an example that is applicable to
recruitment. The question, <code>Do you have experience with managing a sales team?</code> is already
added. A new question is then added, <code>How many years of experience?</code>. This question should <em>only</em>
appear if the applicant selected <code>Yes</code> to the question <code>Do you have prior experience managing a
sales team?</code>.</p>
<p>To properly configure this example, activate the <b>Conditional Display</b> option. Then,
select <code>Do you have experience with managing a sales team?</code> as the <b>Triggering
Question</b>. Then, select <b>Yes</b> for the triggering answer.</p>
<img alt="The layout field when properly configured for a conditional question." class="align-center" src="../../../_images/layout.png"/>
</div>

###### Sessions en direct

If the question is for a live session, activate the **Question Time Limit**
option. A **seconds** field appears. Enter the amount of time allotted for the
applicant to enter the answer, in seconds.

#### Options

Next, configure the various options for the interview form. Click the
**Options** tab to view all the options to configure, by category.

##### Questions

  * **Pagination** : choose how the questions should be displayed.

    * **One page per question** : display a single question on each page.

    * **One page per section** : display each section with the corresponding questions on an individual page.

    * **One page with all the questions** : display all sections and questions at the same time.

  * **Display Progress as** : choose how to display the percentage of questions remaining to answer. This option only appears if either **One page per question** or **One page per section** is selected for **Pagination**.

    * **Percentage left** : display the remaining amount in a percentage (%).

    * **Number** : display the remaining amount in a numerical value.

  * **Question Selection** : choose which questions are presented.

    * **All questions** : display the entire form, with all questions form all sections.

    * **Randomized per Section** : display only a random selection of questions from each section.

  * **Back Button** : activate this option if the applicant is able to click a back button to go back to previous questions.

<div class="alert alert-primary">
<p class="alert-title">
Note</p><p>Although it is a selectable option, the <b>Randomized per section</b> option should only be
used if receiving partial information/an incomplete survey from every applicant is acceptable to
the business.</p>
</div>

##### Temps & Notation

  * **Survey Time Limit** : activate this option to limit the time allowed to complete the form. When selected, a field to enter the minutes appears next to the checked box. Enter the time (using an XX:XX minute/second format) in the field.

  * **Scoring** : choose how the questions should be scored.

    * **No scoring** : select this option to not score the form.

    * **Scoring with answers at the end** : select this option to score the form and display the correct answers for the candidate when they are finished with the form.

    * **Scoring without answers at the end** : select this option to score the form but not display the answers to the candidate.

  * **Required Score (%)** : this option appears if one of the scoring options was selected. Enter the percentage the candidate needs to pass the exam (example, 80.00%). The entry should be written in an “XX.XX” format.

  * **Is a Certification** : activate this option if the form is a certification exam. When activated, a drop-down menu appears next to the checkbox. Select one of the default formats for the PDF certificate that will be sent to the candidate after completing the certification exam. Click the **Preview** button to view an example of the PDF certificate.

  * **Certified Email Template** : if the **Is a Certification** box is activated, a **Certified Email Template** appears. Select the email template from the drop-down menu that is to be used when the applicant passes the test. Click the **External Link** icon to the right of the email template to preview the email.

##### Participants

  * **Access Mode** : specify who can access the exam. Either **Anyone with the link** or **Invited people only**.

  * **Require Login** : activate this option to require candidates to log in before taking the exam, whether they have a valid token or not.

  * **Limit Attempts** : if there is a limit to how many times the exam can be taken, activate this box, then enter the maximum attempt number in the field next to it.

##### Session en direct

  * **Session Code** : enter the access code that will allow the viewers into the live exam session.

  * **Session Link** : the link appears in a box next to the **Session Link** option. Click the **Copy** button to copy the link.

  * **Reward quick answers** : if the exam is to be taken live, activate this option to award more points to participants who answer quickly.

Après avoir saisi tous les champs, cliquez sur le bouton **Enregistrer** pour
enregistrer les changements ou cliquez sur **Ignorer** pour supprimer les
changements.

![Plusieurs options pour configurer le formulaire
d'entretien.](../../../_images/options.png)

#### Description

When the applicant begins the survey, the text entered in this tab appears at
the top of the survey page. Enter any information or descriptions that would
be helpful to the applicant.

#### Message de fin

After the survey is complete, the message entered in this tab is displayed for
the applicant.

