import { searchDog } from "@/pages/api/dog";
import styles from "@/styles/Home.module.css";
import { Inter } from "next/font/google";
import Head from "next/head";
import Carousel from "nuka-carousel/lib/carousel";
import { useState } from "react";

const inter = Inter({ subsets: ["latin"] });
type DogImageProps = {
  initialDogImageUrl: string;
};

export default function Home({ initialDogImageUrl }: DogImageProps) {
  const [dogImage, _] = useState(initialDogImageUrl);

  return (
    <>
      <Head>
        <title>Filmography</title>
        <meta name="description" content="Filmography" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <div className={styles.grid}>
          <h2 className={inter.className}>
            Docs <span>-&gt;</span>
          </h2>
          <p className={inter.className}>
            Find in-depth information about Next.js features and&nbsp;API.
          </p>
        </div>

        <div className={styles.container}>
          <main>
            <h1>犬の画像</h1>
          </main>
          <div style={{ position: "relative", width: 400, height: 400 }}>
            <Carousel>
              <img src={dogImage} alt="犬" />
              <img src={dogImage} alt="犬" />
              <img src={dogImage} alt="犬" />
            </Carousel>
          </div>
        </div>
      </main>
    </>
  );
}

export const getServerSideProps = async () => {
  const res = await searchDog();
  return {
    props: {
      initialDogImageUrl: res.message,
    },
  };
};
