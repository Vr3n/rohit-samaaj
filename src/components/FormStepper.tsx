const FormStepper = () => {
  return (
    <ol className="w-full items-center space-y-4 sm:flex sm:space-x-8 sm:space-y-0">
      <li className="flex items-center space-x-2.5 text-blue-600 dark:text-blue-500">
        <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-blue-600 dark:border-blue-500">
          1
        </span>
        <span>
          <h3 className="font-medium leading-tight">Personal Info</h3>
          <p className="text-sm">Your Basic Info</p>
        </span>
      </li>
      <li className="flex items-center space-x-2.5 text-gray-500 dark:text-gray-400">
        <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-gray-500 dark:border-gray-400">
          2
        </span>
        <span>
          <h3 className="font-medium leading-tight"></h3>
          <p className="text-sm">Step details here</p>
        </span>
      </li>
      <li className="flex items-center space-x-2.5 text-gray-500 dark:text-gray-400">
        <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-gray-500 dark:border-gray-400">
          3
        </span>
        <span>
          <h3 className="font-medium leading-tight">Payment info</h3>
          <p className="text-sm">Step details here</p>
        </span>
      </li>
    </ol>
  );
};

export default FormStepper;
