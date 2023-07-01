import Head from "next/head";
import FormContainer from "~/components/FormContainer";
import FormStepper from "~/components/FormStepper";
import { Card } from "~/components/ui/card";

const SurveyFormLayout = (props: { children: React.ReactNode }) => {
  return (
    <>
      <Head>
        <title>Rohit Samaaj | Survey Form</title>
        <meta name="description" content="rohit samaaj survey form." />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="mx-auto my-2 max-w-2xl">
        <div className="flex flex-col justify-center">
          <h1 className="text-center text-3xl">Rohit Samaaj</h1>
          <p className="mb-4 text-center text-gray-500">
            Census survey for samaaj members.
          </p>
          <FormContainer className="p-4 md:p-0">
            <Card className="my-2 bg-gradient-to-b from-yellow-50 p-4 md:rounded-full">
              <FormStepper />
            </Card>
            {props.children}
          </FormContainer>
        </div>
      </main>
    </>
  );
};

export default SurveyFormLayout;
