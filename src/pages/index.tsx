import { type NextPage } from "next";
import Head from "next/head";
import FormContainer from "~/components/FormContainer";
import FormStepper from "~/components/FormStepper";
import SurveyForm from "~/components/forms/SurveyForm";
import { Card } from "~/components/ui/card";

const Home: NextPage = () => {
  return (
    <>
      <Head>
        <title>Rohit Samaaj | Home</title>
        <meta name="description" content="rohit samaaj home" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="mx-auto my-2 max-w-2xl">
        <div className="flex flex-col justify-center">
          <h1 className="text-center text-3xl">Rohit Samaaj</h1>
          <p className="mb-4 text-center text-gray-500">
            Census survey for samaaj members.
          </p>
          <FormContainer>
            <Card className="my-2 rounded-full bg-gradient-to-b from-yellow-50 p-4">
              <FormStepper />
            </Card>
            <SurveyForm />
          </FormContainer>
        </div>
      </main>
    </>
  );
};

export default Home;
