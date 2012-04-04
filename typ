BEGIN;
CREATE TABLE "nift_nift_user" (
    "login_name_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "sex" varchar(1) NOT NULL,
    "dob" date NOT NULL,
    "phone_no" varchar(15) NOT NULL,
    "user_id" varchar(20) NOT NULL PRIMARY KEY,
    "marital_status" varchar(1) NOT NULL,
    "perm_street" varchar(200) NOT NULL,
    "perm_zip" smallint NOT NULL,
    "perm_state" varchar(50) NOT NULL
)
;
CREATE TABLE "nift_profile" (
    "id" serial NOT NULL PRIMARY KEY,
    "join_date" date NOT NULL,
    "designation" varchar(1) NOT NULL,
    "centre" varchar(2) NOT NULL,
    "room_no" varchar(10) NOT NULL,
    "past_positions" varchar(150) NOT NULL,
    "experience" smallint,
    "expertise" varchar(150) NOT NULL,
    "image" varchar(100) NOT NULL
)
;
CREATE TABLE "nift_attendance" (
    "date" date NOT NULL,
    "present" boolean NOT NULL,
    "user_id_id" varchar(20) NOT NULL PRIMARY KEY REFERENCES "nift_nift_user" ("user_id") DEFERRABLE INITIALLY DEFERRED
)
;
CREATE TABLE "nift_sem_info" (
    "term" varchar(1) NOT NULL,
    "year" varchar(4) NOT NULL,
    "sem_id" serial NOT NULL PRIMARY KEY
)
;
CREATE TABLE "nift_course" (
    "course_name" varchar(50) NOT NULL,
    "course_id" varchar(20) NOT NULL PRIMARY KEY
)
;
CREATE TABLE "nift_cen_dep_info" (
    "centre_name" varchar(50) NOT NULL,
    "department_name" varchar(50) NOT NULL,
    "cen_dep_id" serial NOT NULL PRIMARY KEY
)
;
CREATE TABLE "nift_offered" (
    "sem_id_id" integer NOT NULL REFERENCES "nift_sem_info" ("sem_id") DEFERRABLE INITIALLY DEFERRED,
    "course_id_id" varchar(20) NOT NULL REFERENCES "nift_course" ("course_id") DEFERRABLE INITIALLY DEFERRED,
    "cen_dep_id_id" integer NOT NULL REFERENCES "nift_cen_dep_info" ("cen_dep_id") DEFERRABLE INITIALLY DEFERRED,
    "every_id" serial NOT NULL PRIMARY KEY,
    "user_id_id" varchar(20) NOT NULL REFERENCES "nift_nift_user" ("user_id") DEFERRABLE INITIALLY DEFERRED
)
;
CREATE TABLE "nift_teaching" (
    "study_type" varchar(1) NOT NULL,
    "detail_type" varchar(1) NOT NULL,
    "teaching_id" serial NOT NULL PRIMARY KEY,
    "hours" smallint NOT NULL,
    "every_id_id" integer NOT NULL REFERENCES "nift_offered" ("every_id") DEFERRABLE INITIALLY DEFERRED,
    "user_id_id" varchar(20) NOT NULL REFERENCES "nift_nift_user" ("user_id") DEFERRABLE INITIALLY DEFERRED
)
;
CREATE TABLE "nift_feedback" (
    "week_no" varchar(1) NOT NULL,
    "avg_content_rat" smallint,
    "avg_present_rat" smallint,
    "feedback_id" serial NOT NULL PRIMARY KEY,
    "every_id_id" integer NOT NULL REFERENCES "nift_offered" ("every_id") DEFERRABLE INITIALLY DEFERRED
)
;
CREATE TABLE "nift_leave_info" (
    "leave_type" varchar(1) NOT NULL,
    "start_date" date NOT NULL,
    "reason" varchar(1000) NOT NULL,
    "no_of_days" smallint NOT NULL,
    "approved" boolean NOT NULL,
    "days_left" smallint NOT NULL,
    "user_id_id" varchar(20) NOT NULL REFERENCES "nift_nift_user" ("user_id") DEFERRABLE INITIALLY DEFERRED,
    "leave_id" serial NOT NULL PRIMARY KEY
)
;
CREATE TABLE "nift_leave_extension_info" (
    "last_leave_id_id" integer NOT NULL REFERENCES "nift_leave_info" ("leave_id") DEFERRABLE INITIALLY DEFERRED,
    "reason" varchar(1000) NOT NULL,
    "approved" boolean NOT NULL,
    "no_of_days" smallint NOT NULL,
    "eleave_id" serial NOT NULL PRIMARY KEY
)
;
CREATE INDEX "nift_offered_sem_id_id" ON "nift_offered" ("sem_id_id");
CREATE INDEX "nift_offered_course_id_id" ON "nift_offered" ("course_id_id");
CREATE INDEX "nift_offered_course_id_id_like" ON "nift_offered" ("course_id_id" varchar_pattern_ops);
CREATE INDEX "nift_offered_cen_dep_id_id" ON "nift_offered" ("cen_dep_id_id");
CREATE INDEX "nift_offered_user_id_id" ON "nift_offered" ("user_id_id");
CREATE INDEX "nift_offered_user_id_id_like" ON "nift_offered" ("user_id_id" varchar_pattern_ops);
CREATE INDEX "nift_teaching_every_id_id" ON "nift_teaching" ("every_id_id");
CREATE INDEX "nift_teaching_user_id_id" ON "nift_teaching" ("user_id_id");
CREATE INDEX "nift_teaching_user_id_id_like" ON "nift_teaching" ("user_id_id" varchar_pattern_ops);
CREATE INDEX "nift_feedback_every_id_id" ON "nift_feedback" ("every_id_id");
CREATE INDEX "nift_leave_info_user_id_id" ON "nift_leave_info" ("user_id_id");
CREATE INDEX "nift_leave_info_user_id_id_like" ON "nift_leave_info" ("user_id_id" varchar_pattern_ops);
CREATE INDEX "nift_leave_extension_info_last_leave_id_id" ON "nift_leave_extension_info" ("last_leave_id_id");
COMMIT;
