from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField


class DescriptiveSelectField(SelectField):
    """
    DescriptiveSelectField is a custom field that extends the SelectField
    class from the WTforms library.

    This field is used to create a select field with descriptive options.

    Attributes:
        # choices: A list of tuples containing the field values and descriptions.
        # description: A description of the field.
    """

    def __init__(self, label='', validators=None, choices=None, description='', **kwargs):
        super(DescriptiveSelectField, self).__init__(
            label=label, validators=validators, choices=choices, **kwargs)
        self.description = description


class SurveyForm(FlaskForm):
    """
    Survey Form will be used to collect user input data for
    the machine learning model prediction.

    Attributes:
        # General Health Section

        poorhlth: The user's general health.
        physhlth: The user's physical health.
        genhlth: The user's general health.
        diffwalk: The user's difficulty walking.
        diffalon: The user's difficulty walking alone.
        checkup1: The user's checkup status.

        # Mental Health Section

        addepev3: The user's mental health.
        acedeprs: The user's depression.
        sdlonely: The user's loneliness.
        lsatisfy: The user's life satisfaction.
        emtsuprt: The user's emotional support.
        decide: The user's decision making.
        cdsocia1: The user's socializing.

        # Lifestyle and Habits Section

        smokday2: The user's smoking habits.
        alcday4: The user's alcohol consumption.
        marijan1: The user's marijuana consumption.
        exeroft1: The user's exercise habits.
        usenow3: The user's drug use.

        # Socioeconomic Factors Section

        income3: The user's income status.
        educa: The user's education status.
        employ1: The user's employment status.
        marital: The user's marital status.
        _state: The user's state.
    """

    # General Health Section
    poorhlth = DescriptiveSelectField(
        label='Poor Health',  # POORHLTH
        choices=[('', ''), ('Yes', 'Yes'),
                 ('No', 'No'), ('Not Sure', 'Not Sure')],
        description="During the past 30 days, for about how many days did poor physical or mental health keep you from doing your usual activities, such as self-care, work, or recreation?",
        validators=[DataRequired()]
    )
    physhlth = DescriptiveSelectField(
        label='Physical Health',  # PHYSHLTH
        choices=[('', ''), ('Yes', 'Yes'),
                 ('No', 'No'), ('Not Sure', 'Not Sure')],
        description="About your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good?",
        validators=[DataRequired()]
    )
    genhlth = DescriptiveSelectField(
        label='General Health',  # GENHLTH
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Not Sure', 'Not Sure')],
        description="Would you say that in general your health is:", validators=[DataRequired()]
    )
    diffwalk = DescriptiveSelectField(
        label='Difficulty walking',  # DIFFWALK
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Not Sure', 'Not Sure')],
        description="Do you have serious difficulty walking or climbing stairs?", validators=[DataRequired()]
    )
    diffalon = DescriptiveSelectField(
        label='Difficulty doing errands alone',  # DIFFALON
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Not Sure', 'Not Sure')],
        description="Because of a physical, mental, or emotional condition, do you have difficulty doing errands alone such as visiting a doctor´s office or shopping?", validators=[DataRequired()]
    )
    checkup1 = DescriptiveSelectField(
        label='Length of time since last routine checkup',  # CHECKUP1
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Not Sure', 'Not Sure')],
        description="Describe your general health status. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.",
        validators=[DataRequired()]
    )

    # Mental Health Section
    addepev3 = DescriptiveSelectField(
        label='(Ever told) you had a depressive disorder',  # ADDEPEV3
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Sometimes', 'Sometimes')],
        description="(Ever told) (you had) a depressive disorder (including depression, major depression, dysthymia, or minor depression)?",
        validators=[DataRequired()]
    )
    acedeprs = DescriptiveSelectField(
        label='Live With Anyone Depressed, Mentally Ill, Or Suicidal?',  # ACEDEPRS
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Sometimes', 'Sometimes')],
        description="Did you live with anyone who was depressed, mentally ill, or suicidal?",
        validators=[DataRequired()]
    )
    sdlonely = DescriptiveSelectField(
        label='How often do you feel lonely?',  # SDLONELY
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Sometimes', 'Sometimes')],
        description="How often do you feel lonely?  Is it…", validators=[DataRequired()]
    )
    lsatisfy = DescriptiveSelectField(
        label='Satisfaction with life',  # LSATISFY
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Sometimes', 'Sometimes')],
        description="In general, how satisfied are you with your life?", validators=[DataRequired()]
    )
    emtsuprt = DescriptiveSelectField(
        label='How often get emotional support needed',  # EMTSUPRT
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Sometimes', 'Sometimes')],
        description="How often do you get the social and emotional support you need?", validators=[DataRequired()]
    )
    decide = DescriptiveSelectField(
        label='Difficulty Concentrating or Remembering',  # DECIDE
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Sometimes', 'Sometimes')],
        description="Because of a physical, mental, or emotional condition, do you have serious difficulty concentrating, remembering, or making decisions?", validators=[DataRequired()]
    )
    cdsocia1 = DescriptiveSelectField(
        label='Does difficulties with thinking or memory interfere with work or social activities',  # CDSOCIA1
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No'),
                 ('Sometimes', 'Sometimes')],
        description="During the past 12 months, have your difficulties with thinking or memory interfered with your ability to work or volunteer?", validators=[DataRequired()]
    )

    # Lifestyle and Habits Section
    smokday2 = DescriptiveSelectField(
        label='Frequency of Days Now Smoking',  # SMOKDAY2
        choices=[('', ''), ('Daily', 'Daily'),
                 ('Occasionally', 'Occasionally'), ('Never', 'Never')],
        description=" Do you now smoke cigarettes every day, some days, or not at all?", validators=[DataRequired()]
    )
    alcday4 = DescriptiveSelectField(
        label='Days in past 30 had alcoholic beverage',  # ALCDAY4
        choices=[('', ''), ('Daily', 'Daily'),
                 ('Occasionally', 'Occasionally'), ('Never', 'Never')],
        description="During the past 30 days, how many days per week or per month did you have at least one drink of any alcoholic beverage?  (A 40 ounce beer would count as 3 drinks, or a cocktail drink with 2 shots would count as 2 drinks.)", validators=[DataRequired()]
    )
    marijan1 = DescriptiveSelectField(
        label='During the past 30 days, on how many days did you use marijuana or hashish?',  # MARIJAN1
        choices=[('', ''), ('Daily', 'Daily'),
                 ('Occasionally', 'Occasionally'), ('Never', 'Never')],
        description="During the past 30 days, on how many days did you use marijuana or cannabis?",
        validators=[DataRequired()]
    )
    exeroft1 = DescriptiveSelectField(
        label='How Many Times Walking, Running, Jogging, or Swimming',  # EXEROFT1
        choices=[('', ''), ('Daily', 'Daily'),
                 ('Occasionally', 'Occasionally'), ('Never', 'Never')],
        description="How many times per week or per month did you take part in this activity during the past month?",
        validators=[DataRequired()]
    )
    usenow3 = DescriptiveSelectField(
        label='Use of Smokeless Tobacco Products',  # USENOW3
        choices=[('', ''), ('Daily', 'Daily'),
                 ('Occasionally', 'Occasionally'), ('Never', 'Never')],
        description="Do you currently use chewing tobacco, snuff, or snus every day, some days, or not at all?  (Snus (Swedish for snuff) is a moist smokeless tobacco, usually sold in small pouches that are placed under the lip against the gum.)", validators=[DataRequired()]
    )

    # Socioeconomic Factors Section
    income3 = DescriptiveSelectField(
        label='Income Level',  # INCOME3
        choices=[('', ''), ('Low', 'Low'),
                 ('Medium', 'Medium'), ('High', 'High')],
        description="Is your annual household income from all sources:  (If respondent refuses at any income level, code ´Refused.´)",
        validators=[DataRequired()]
    )
    educa = DescriptiveSelectField(
        label='Education Level',  # EDUCA
        choices=[('', ''), ('High School', 'High School'), ('Bachelor`s',
                                                            'Bachelor`s'), ('Master`s', 'Master`s'), ('Doctorate', 'Doctorate')],
        description="What is the highest grade or year of school you completed?",
        validators=[DataRequired()]
    )
    employ1 = DescriptiveSelectField(
        label='Employment Status',  # EMPLOY1
        choices=[('', ''), ('Employed', 'Employed'),
                 ('Unemployed', 'Unemployed'), ('Retired', 'Retired')],
        description="Are you currently…?", validators=[DataRequired()]
    )
    marital = DescriptiveSelectField(
        label='Marital Status',  # MARITAL
        choices=[('', ''), ('Single', 'Single'), ('Married', 'Married'),
                 ('Divorced', 'Divorced'), ('Widowed', 'Widowed')],
        description="Are you: (marital status)", validators=[DataRequired()]
    )
    state = DescriptiveSelectField(
        label='State',  # STATE
        choices=[('', ''), ('State1', 'State1'),
                 ('State2', 'State2'), ('State3', 'State3')],
        description="Which state do you reside in.",
        validators=[DataRequired()]
    )
    sdhbills = DescriptiveSelectField(
        label='Were you not able to pay your bills?',  # SDHBILLS
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="During the last 12 months, was there a time when you were not able to pay your mortgage, rent or utility bills?",
        validators=[DataRequired()]
    )
    sdhemple = DescriptiveSelectField(
        label='Have you lost employment or had hours reduced?',  # SDHEMPLY
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="In the past 12 months have you lost employment or had hours reduced?",
        validators=[DataRequired()]
    )
    sdhfood1 = DescriptiveSelectField(
        label='How often did the food that you bought not last, and you \
            didn’t have money to get more?',  # SDHFOOD1
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="During the past 12 months how often did the food \
            that you bought not last, and you didn’t have money to get more? Was that…",
        validators=[DataRequired()]
    )
    sdhstre1 = DescriptiveSelectField(
        label='How often have you felt this kind of stress?',  # SDHSTRE1
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="Within the last 30 days, how often have you felt this kind of stress?",
        validators=[DataRequired()]
    )
    sdhutils = DescriptiveSelectField(
        label='Were you not able to pay utility bills or threatened to lose service?',  # SDHUTILS
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="During the last 12 months was there a time when an \
            electric, gas, oil, or water company threatened to shut off \
            services?",
        validators=[DataRequired()]
    )
    sdhtrnsp = DescriptiveSelectField(
        label='Has a lack of reliable transportation kept you from appointments, meetings, work, or getting things needed',  # SDHTRNSP
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="During the past 12 months has a lack of reliable transportation kept you from medical appointments, meetings, work, or from getting things needed for daily living?",
        validators=[DataRequired()]
    )
    cdshous1 = DescriptiveSelectField(
        label='Given up day-to-day chores due to difficulties with thinking or memory',  # CDSHOUS1
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="During the past 12 months, have your difficulties with thinking or memory interfered with day-to-day activities, such as managing medications, paying bills, or keeping track of appointments?", validators=[DataRequired()]
    )

    # Chronic Conditions and Medical History Section
    hvarth4 = DescriptiveSelectField(
        label='Told Had Arthritis',  # HAVARTH4
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="(Ever told) (you had) some form of arthritis, rheumatoid \
            arthritis, gout, lupus, or fibromyalgia?  (Arthritis diagnoses include: \
            rheumatism, polymyalgia rheumatica; osteoarthritis (not osteporosis); \
            tendonitis, bursitis, bunion, tennis elbow; carpal tunnel syndrome, \
            tarsal tunnel syndrome; joint infection, etc.)",
        validators=[DataRequired()]
    )
    diabete4 = DescriptiveSelectField(
        label='(Ever told) you had diabetes',  # DIABETE4
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="(Ever told) (you had) diabetes?  (If ´Yes´ and respondent \
            is female, ask ´Was this only when you were pregnant?´. \
             If Respondent says pre-diabetes or borderline diabetes, \
             use response code 4.)",
        validators=[DataRequired()]
    )
    cholchk3 = DescriptiveSelectField(
        label='How Long since Cholesterol Checked', choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="About how long has it been since you last had your cholesterol checked?",
        validators=[DataRequired()]
    )
    bpmeds1 = DescriptiveSelectField(
        label='Currently Taking Prescription Blood Pressure Medication',  # BPMEDS1
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="Are you currently taking prescription medicine for your high blood pressure?",
        validators=[DataRequired()]
    )
    bphigh6 = DescriptiveSelectField(
        label='Ever Told Blood Pressure High',  # BPHIGH6
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="Have you ever been told by a doctor, nurse or other \
            health professional that you have high blood pressure?  \
            (If ´Yes´ and respondent is female, ask ´Was this only when \
            you were pregnant?´.)",
        validators=[DataRequired()]
    )
    cvdstrk3 = DescriptiveSelectField(
        label='Ever Diagnosed with a Stroke',  # CVDSTRK3
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="(Ever told) (you had) a stroke.",
        validators=[DataRequired()]
    )
    cvdcrhd4 = DescriptiveSelectField(
        label='Ever Diagnosed with Angina or Coronary Heart Disease',  # CVDCRHD4
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="(Ever told) (you had) angina or coronary heart disease?",
        validators=[DataRequired()]
    )
    chckdny2 = DescriptiveSelectField(
        label='Ever told you have kidney disease?',  # CHCKDNY2
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="Not including kidney stones, bladder infection or \
            incontinence, were you ever told you had kidney disease?",
        validators=[DataRequired()]
    )
    cholmed3 = DescriptiveSelectField(
        label='Currently taking medicine for high cholesterol',  # CHOLMED3
        choices=[('', ''), ('Yes', 'Yes'), ('No', 'No')],
        description="Are you currently taking medicine prescribed by your \
            doctor or other health professional for your cholesterol?",
        validators=[DataRequired()]
    )

    # Submit Button
    submit = SubmitField('Submit')
