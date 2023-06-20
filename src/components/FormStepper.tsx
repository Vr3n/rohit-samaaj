import { BookOpenCheck, IndianRupee, PhoneCall, User } from "lucide-react";

const FormStepperItem = (props: {
  stepperIcon: React.ReactNode;
  title: string;
  description: string;
}) => {
  return (
    <li className="text-grey-600 flex items-center space-x-2.5 dark:text-blue-500">
      <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full border border-black dark:border-blue-500">
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
  },
  {
    icon: <PhoneCall />,
    title: "Contact Details",
    description: "Phone, Email, and Address.",
  },
  {
    icon: <BookOpenCheck />,
    title: "Educational Qualification",
    description: "Your recent / max education.",
  },
  {
    icon: <IndianRupee />,
    title: "Income Details",
    description: "Your family income details.",
  },
];

const FormStepper = () => {
  return (
    <ol className="w-full items-center space-y-4 sm:flex sm:space-x-8 sm:space-y-0">
      {stepperData.map((stepper, idx) => (
        <FormStepperItem
          key={idx}
          description={stepper.description}
          title={stepper.title}
          stepperIcon={stepper.icon}
        />
      ))}
    </ol>
  );
};

export default FormStepper;
