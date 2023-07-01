"use client";

import { BookOpenCheck, IndianRupee, PhoneCall, User } from "lucide-react";
import { usePathname } from "next/navigation";
import { cn } from "~/lib/utils";

const FormStepperItem = (props: {
  stepperIcon: React.ReactNode;
  title: string;
  description: string;
  className?: string;
}) => {
  return (
    <li className={cn(props.className, "flex items-center space-x-2.5")}>
      <span
        className={cn(
          props.className,
          "flex h-12 w-12 shrink-0 items-center justify-center rounded-full border"
        )}
      >
        {props.stepperIcon}
      </span>
      <span>
        <h3 className="text-xs font-medium leading-tight">{props.title}</h3>
        {/* <p className="text-xs">{props.description}</p> */}
      </span>
    </li>
  );
};

const stepperData = [
  {
    icon: <User />,
    title: "Personal Info",
    description: "Basic info about member.",
    link: "personal-details",
  },
  {
    icon: <PhoneCall />,
    title: "Contact Details",
    description: "Phone, Email, and Address.",
    link: "contact-details",
  },
  {
    icon: <BookOpenCheck />,
    title: "Educational Qualification",
    description: "Your recent / max education.",
    link: "educational-qualification",
  },
  {
    icon: <IndianRupee />,
    title: "Income Details",
    description: "Your family income details.",
    link: "income-details",
  },
];

const ACTIVE_STEPPER_CLASSNAME = "text-blue-500 border-blue-500";
const NORMAL_STEPPER_CLASSNAME = "text-grey-600 border-grey-800";

const FormStepper = () => {
  const pathName = usePathname();
  const activePath = pathName.split("/").slice(-1)[0];
  return (
    <ol className="w-full items-center space-y-4 sm:flex sm:space-x-8 sm:space-y-0">
      {stepperData.map((stepper, idx) => (
        <FormStepperItem
          key={idx}
          description={stepper.description}
          title={stepper.title}
          stepperIcon={stepper.icon}
          className={
            stepper.link === activePath
              ? ACTIVE_STEPPER_CLASSNAME
              : NORMAL_STEPPER_CLASSNAME
          }
        />
      ))}
    </ol>
  );
};

export default FormStepper;
