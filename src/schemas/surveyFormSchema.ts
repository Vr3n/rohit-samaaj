import z from "zod";
import { nationalityList } from "~/constants/nationalityList";

const NationalityEnum = z.enum(nationalityList);

const AddressSchema = z.object({
  flatNoBuildingName: z
    .string({ required_error: "Flat number or Building Name is required" })
    .min(3),
  area: z.string({ required_error: "Enter your area name." }).min(2),
  landmark: z.string().optional(),
  district: z.string({ required_error: "District is required" }).min(2),
  taluka: z.string({ required_error: "Taluka is required." }).min(2),
  city: z.string({ required_error: "City name is required." }).min(2),
  pincode: z.string({ required_error: "Pincode is required" }).min(6).max(6),
});

const EmploymentStatusSchema = z.object({
  companyName: z.string({ required_error: "company name is required." }),
  designation: z.string({ required_error: "Designation is required." }),
});

const AadharValidation = z
  .string({ required_error: "Aadhar number is required." })
  .regex(new RegExp(/^[0-9]{10}$/), {
    message: "Aadhar number should be exactly 10 digits.",
  })
  .max(10, {
    message: "maximum 10 digits allowed.",
  });

export const surveyFormSchema = z.object({
  nationality: NationalityEnum,
  aadharNumber: AadharValidation,
  firstName: z
    .string({ required_error: "First Name is required." })
    .min(1, { message: "First Name is required." }),
  lastName: z
    .string({ required_error: "Last Name is required." })
    .min(1, { message: "Last Name is required." }),
  fatherName: z.string(),
  motherName: z.string(),
});
