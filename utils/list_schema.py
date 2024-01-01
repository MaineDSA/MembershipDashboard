from pandera import DataFrameSchema, Column, Check, Index

STATE_ABBR = [
    "AK",
    "AL",
    "AR",
    "AZ",
    "CA",
    "CO",
    "CT",
    "DC",
    "DE",
    "FL",
    "GA",
    "HI",
    "IA",
    "ID",
    "IL",
    "IN",
    "KS",
    "KY",
    "LA",
    "MA",
    "MD",
    "ME",
    "MI",
    "MN",
    "MO",
    "MS",
    "MT",
    "NC",
    "ND",
    "NE",
    "NH",
    "NJ",
    "NM",
    "NV",
    "NY",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VA",
    "VT",
    "WA",
    "WI",
    "WV",
    "WY",
]


class MembershipData:
    DUES_STATUS = ["past_due", "overdue", "never", "lapsed", "active", "canceled_by_admin", "canceled_by_failure", "canceled_by_processor", "canceled_by_user"]
    MEMBERSHIP_TYPE = ["yearly", "monthly", "one-time", "lifetime", "income-based"]
    MEMBERSHIP_STATUS = ["member in good standing", "member", "lapsed"]
    UNION_MEMBER_STATUS = [
        "Yes",
        "Yes, current union member",
        "Currently organizing my workplace",
        "No",
        "No, not a union member",
        "No, but former union member",
    ]
    STUDENT_STATUS = ["No", "Yes", "Yes, college student", "Yes, high school student"]
    MAILING_PREF = ["Membership card only", "No", "Yes"]


schema = DataFrameSchema(
    columns={
        "first_name": Column(
            dtype="string",
            checks=None,
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="First Name",
        ),
        "middle_name": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Middle Name or Initial",
        ),
        "last_name": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Last Name",
        ),
        "email": Column(
            dtype="string",
            checks=None,
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Email Address",
        ),
        "do_not_call": Column(
            dtype="boolean",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Do Not Call",
        ),
        "p2ptext_optout": Column(
            dtype="boolean",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Do Not Text",
        ),
        "best_phone": Column(
            dtype="string",
            checks=Check.str_matches(r"^[a-z0-9-]+$"),
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Best Phone",
        ),
        "mobile_phone": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Mobile Phone",
        ),
        "home_phone": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Home Phone",
        ),
        "work_phone": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Work Phone",
        ),
        "join_date": Column(
            dtype="string",
            checks=Check.str_matches(r"^\d{4}-0?\d+-0?\d+$"),
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Membership Original Join Date",
        ),
        "xdate": Column(
            dtype="string",
            checks=Check.str_matches(r"^\d{4}-0?\d+-0?\d+$"),
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Membership Expiration Date",
        ),
        "membership_type": Column(
            dtype="string",
            checks=Check.isin(MembershipData.MEMBERSHIP_TYPE),
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Membership Type",
        ),
        "monthly_dues_status": Column(
            dtype="string",
            checks=Check.isin(MembershipData.DUES_STATUS),
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Monthly Dues Status",
        ),
        "yearly_dues_status": Column(
            dtype="string",
            checks=Check.isin(MembershipData.DUES_STATUS),
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Yearly Dues Status",
        ),
        "membership_status": Column(
            dtype="string",
            checks=Check.isin(MembershipData.MEMBERSHIP_STATUS),
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Membership Status",
        ),
        "memb_status_letter": Column(
            dtype="string",
            checks=None,
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Membership Status Letter",
        ),
        "union_member": Column(
            dtype="string",
            checks=Check.isin(MembershipData.UNION_MEMBER_STATUS),
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Union - Status",
        ),
        "union_name": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Union - Name",
        ),
        "union_local": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Union - Local",
        ),
        "accommodations": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Accommodations",
        ),
        "race": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Race",
        ),
        "student_yes_no": Column(
            dtype="string",
            checks=Check.isin(MembershipData.STUDENT_STATUS),
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Student - Status",
        ),
        "student_school_name": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Student - School Name",
        ),
        "mailing_pref": Column(
            dtype="string",
            checks=Check.isin(MembershipData.MAILING_PREF),
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Mailing Preference",
        ),
        "address1": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Address Line 1",
        ),
        "address2": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Address Line 2",
        ),
        "city": Column(
            dtype="string",
            checks=None,
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="City",
        ),
        "state": Column(
            dtype="string",
            checks=Check.isin(STATE_ABBR),
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="State",
        ),
        "zip": Column(
            dtype="string",
            checks=None,
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="ZIP Code",
        ),
        "country": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Country",
        ),
        "dsa_chapter": Column(
            dtype="string",
            checks=None,
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="DSA Chapter Name",
        ),
        "ydsa_chapter": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="yDSA Chapter Name",
        ),
        "congressional_district": Column(
            dtype="string",
            checks=None,
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="Congressional District",
        ),
        "membership_length": Column(
            dtype="int32",
            checks=Check.greater_than_or_equal_to(min_value=0.0),
            nullable=False,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description="Does not account for gaps in membership.",
            title="Membership Length (Years)",
        ),
        "lon": Column(
            dtype="float32",
            checks=[
                Check.greater_than_or_equal_to(min_value=-180),
                Check.less_than_or_equal_to(max_value=180),
            ],
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description="Used for mapping members on a map.",
            title="Longitude",
        ),
        "lat": Column(
            dtype="float32",
            checks=[
                Check.greater_than_or_equal_to(min_value=-90),
                Check.less_than_or_equal_to(max_value=90),
            ],
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description="Used for mapping members on a map.",
            title="Latitude",
        ),
        "branch": Column(
            dtype="string",
            checks=None,
            nullable=True,
            unique=False,
            coerce=True,
            required=True,
            regex=False,
            description=None,
            title="DSA Chapter Branch",
        ),
    },
    checks=None,
    index=Index(
        dtype="int64",
        checks=None,
        nullable=False,
        coerce=True,
        name="actionkit_id",
        description=None,
        title="Actionkit ID",
    ),
    dtype=None,
    coerce=True,
    strict=False,
    name=None,
    ordered=False,
    unique=None,
    report_duplicates="all",
    unique_column_names=False,
    add_missing_columns=True,
    title="DSA Membership List",
    description=None,
)
