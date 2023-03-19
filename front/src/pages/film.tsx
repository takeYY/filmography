import type { NextPage } from "next";

import styles from "@/styles/Home.module.css";
import Head from "next/head";

const Film: NextPage = () => {
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
          <p>映画</p>
          <p>映画です</p>
          <p>映画です！</p>
          <p>映画です！</p>
          <p>映画です！</p>
          <p>映画です！</p>
          <p>映画です！</p>
        </div>
      </main>
    </>
  );
};

export default Film;
