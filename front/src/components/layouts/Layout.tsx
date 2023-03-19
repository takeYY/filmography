import styles from "@/components/layouts/Layout.module.scss";
import Link from "next/link";
import { useRouter } from "next/router";
import { memo, ReactNode, useState, VFC } from "react";
import { GiDramaMasks, GiFilmProjector, GiFilmStrip } from "react-icons/gi";

import { AiTwotoneHome } from "react-icons/ai";

type Props = {
  children: ReactNode;
};

type Navigation = {
  pageName: string;
  path: string;
  icon: JSX.Element;
};

const navigations: Navigation[] = [
  {
    pageName: "トップ",
    path: "/",
    icon: <AiTwotoneHome />,
  },
  {
    pageName: "映画",
    path: "/film",
    icon: <GiFilmProjector />,
  },
  {
    pageName: "ドラマ",
    path: "/drama",
    icon: <GiDramaMasks />,
  },
  {
    pageName: "アニメ",
    path: "/animation",
    icon: <GiFilmStrip />,
  },
];

/* eslint-disable-next-line react/display-name */
export const Layout: VFC<Props> = memo((props) => {
  const { children } = props;

  const [menuOpen, setMenuOpen] = useState(true);

  const router = useRouter();

  const isPageActive = (pagePath: string): boolean => {
    return pagePath === String(router.route);
  };

  return (
    <div className={styles.root}>
      <aside
        className={styles.sidebar}
        style={{ width: menuOpen ? "200px" : "60px" }}
      >
        <div
          className={styles.hamburger}
          role="button"
          onClick={() => setMenuOpen(!menuOpen)}
        >
          {[...Array(3)].map((_, index: number) => (
            <span
              className={
                menuOpen ? styles.menuCloseArrow : styles.menuOpenArrow
              }
              key={index}
            ></span>
          ))}
        </div>
        {navigations.map((navigation) => (
          <Link href={navigation.path} key={navigation.pageName}>
            <div
              className={styles.flexContainer}
              style={{
                background: isPageActive(navigation.path) ? "#1B555A" : "none",
              }}
            >
              {navigation.icon}
              {menuOpen && (
                <p className={styles.pageName}>{navigation.pageName}</p>
              )}
            </div>
          </Link>
        ))}
      </aside>

      <main className={styles.mainContent}>{children}</main>
    </div>
  );
});
