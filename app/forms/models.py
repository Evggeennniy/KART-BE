from django.db import models
from django.utils.translation import gettext_lazy as _


class ApplicationForm(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Applicant Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone Number"))
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Submission Date"))

    def __str__(self):
        return f"Application form {self.name}"

    class Meta:
        verbose_name = _("Application Form")
        verbose_name_plural = _("Application Forms")


class DealerApplicationForm(models.Model):
    EXPERIENCE_YEARS_CHOICES = [
        ("<1", _("Less than 1 year")),
        ("1-3", _("1–3 years")),
        ("3-5", _("3–5 years")),
        (">5", _("More than 5 years")),
    ]

    LICENSE_STATUS_CHOICES = [
        ("yes", _("Yes")),
        ("no", _("No")),
        ("progress", _("In Progress")),
    ]

    company_name = models.CharField(max_length=32,  verbose_name=_("Company"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    contact_person = models.CharField(max_length=64,  verbose_name=_("Contact Person"))
    position = models.CharField(max_length=255, verbose_name=_("Position"))
    phone = models.CharField(max_length=50,  verbose_name=_("Phone"))
    email = models.EmailField(verbose_name=_("Email"))
    website = models.URLField(blank=True, verbose_name=_("Website"))
    instagram = models.URLField(blank=True, verbose_name=_("Instagram"))
    other_socials = models.TextField(blank=True, verbose_name=_("Other Social Media"))
    experience_years = models.CharField(
        max_length=16,
        choices=EXPERIENCE_YEARS_CHOICES,
        verbose_name=_("Years of Experience")
    )
    main_activity = models.CharField(max_length=64, verbose_name=_("Main Business Direction"))
    license_status = models.CharField(
        max_length=32,
        choices=LICENSE_STATUS_CHOICES,
        verbose_name=_("License Status")
    )
    trains_masters = models.CharField(max_length=32,  verbose_name=_("Do You Train Masters?"))
    has_training_center = models.BooleanField(default=False, verbose_name=_("Has Training Center"))
    seats_count = models.CharField(max_length=32,  verbose_name=_("Seats in Training Room"))
    certified_trainers = models.CharField(max_length=128, verbose_name=_("Certified Trainers"))
    has_office = models.BooleanField(default=False, verbose_name=_("Physical Location / Showroom"))
    distribution_method = models.CharField(max_length=255, verbose_name=_("Product Distribution Method"))
    can_store_products = models.BooleanField(default=False, verbose_name=_("Storage & Logistics Capability"))
    marketing_channels = models.TextField(blank=True, verbose_name=_("Marketing Channels"))
    use_brand_materials = models.BooleanField(default=False, verbose_name=_("Willing to Use KART Marketing Materials"))
    client_base = models.CharField(max_length=32,  verbose_name=_("Active Client Base (Approx.)"))
    target_region = models.CharField(max_length=255, verbose_name=_("Target Region for KART Sales"))
    current_brands = models.TextField(blank=True, verbose_name=_("Currently Represented Brands"))
    cooperation_reason = models.TextField(blank=True, verbose_name=_("Reason for Cooperation with KART"))
    comments = models.TextField(blank=True, verbose_name=_("Additional Comments"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Submission Date"))

    class Meta:
        verbose_name = _("Dealer Application")
        verbose_name_plural = _("Dealer Applications")

    def __str__(self):
        return self.company_name


class InstructorApplicationForm(models.Model):
    ROLE_CHOICES = [
        ("master", _("Pedicure Master")),
        ("podologist", _("Practicing Podologist")),
    ]

    EXPERIENCE_YEARS_CHOICES = [
        ("1-3", _("1–3 years")),
        ("4-5", _("4–5 years")),
        ("6-10", _("6–10 years")),
        ("10+", _("More than 10 years")),
    ]

    TEACHING_VOLUME_CHOICES = [
        ("1-5", _("1–5 students")),
        ("6-10", _("6–10 students")),
        ("11-20", _("11–20 students")),
        ("20+", _("More than 20")),
    ]

    KART_USAGE_CHOICES = [
        ("<1", _("Less than 1 year")),
        ("1-2", _("1–2 years")),
        ("3-5", _("3–5 years")),
        (">5", _("More than 5 years")),
        ("no", _("Do not use")),
    ]

    TRAINING_PLACE_CHOICES = [
        ("yes", _("Yes")),
        ("no", _("No")),
        ("rent", _("Can Rent if Needed")),
    ]

    FAMILIARITY_CHOICES = [
        ("yes", _("Yes")),
        ("no", _("No")),
        ("partly", _("Partly")),
    ]

    name = models.CharField(max_length=64, verbose_name=_("Full Name"))
    birth_date = models.DateField(verbose_name=_("Date of Birth"))
    city = models.CharField(max_length=64, verbose_name=_("City"))
    email = models.EmailField(verbose_name=_("Email"))
    country_code = models.CharField(max_length=8, verbose_name=_("Country Code"))
    phone_number = models.CharField(max_length=32, verbose_name=_("Phone Number"))
    social_links = models.TextField(blank=True, verbose_name=_("Social Media Links"))
    website = models.URLField(blank=True, verbose_name=_("Website"))
    role = models.CharField(
        max_length=16,
        choices=ROLE_CHOICES,
        verbose_name=_("Your Role")
    )
    education = models.TextField(verbose_name=_("Education Background"))
    has_medical_education = models.BooleanField(default=False, verbose_name=_("Medical Education"))
    experience_years = models.CharField(
        max_length=8,
        choices=EXPERIENCE_YEARS_CHOICES,
        verbose_name=_("Years of Experience")
    )
    current_job = models.CharField(max_length=255, verbose_name=_("Current Job & Position"))
    pedicure_techniques = models.TextField(verbose_name=_("Pedicure Techniques You Use"))
    teaches = models.BooleanField(default=False, verbose_name=_("Teaching Experience"))
    course_description = models.TextField(blank=True, verbose_name=_("Course Topics Description"))
    has_training_place = models.CharField(
        max_length=64,
        choices=TRAINING_PLACE_CHOICES,
        verbose_name=_("Training Place Availability")
    )
    students_per_month = models.CharField(
        max_length=16,
        choices=TEACHING_VOLUME_CHOICES,
        verbose_name=_("Students per Month")
    )
    familiar_with_kart = models.CharField(
        max_length=16,
        choices=FAMILIARITY_CHOICES,
        verbose_name=_("Familiar with KART")
    )
    kart_usage_period = models.CharField(
        max_length=8,
        choices=KART_USAGE_CHOICES,
        verbose_name=_("KART Usage Period")
    )
    strengths = models.TextField(verbose_name=_("Your Strengths as a Trainer"))
    audience_experience = models.TextField(verbose_name=_("Audience Experience (Offline/Online)"))
    promotion_channels = models.TextField(verbose_name=_("Promotion Platforms/Channels"))
    motivation = models.TextField(verbose_name=_("Why You Want to Become a KART Instructor"))
    ready_for_training = models.BooleanField(default=False, verbose_name=_("Ready to Join Instructor Program"))
    comments = models.TextField(blank=True, verbose_name=_("Additional Comments"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Submitted At"))

    class Meta:
        verbose_name = _("Instructor Application")
        verbose_name_plural = _("Instructor Applications")

    def __str__(self):
        return self.name
