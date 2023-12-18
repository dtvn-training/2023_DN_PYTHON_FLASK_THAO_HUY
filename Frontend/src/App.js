import React, { lazy, Suspense } from "react";
import PrivateRoute from "./router/PrivateRoute";
import { Routes, Route} from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Loading from "./components/Loading/Loading";

const LazyLoginPage = lazy(() => import("./views/LoginPage/LoginPage"));
const LazyHomePage = lazy(() => import("./views/HomePage/HomePage"));

function App() {
  return (
    <>
      <div className="App">
        <Loading />
        <Suspense fallback={"loading..."}>
          <Routes>
            <Route exact path="/" element={<PrivateRoute />}>
              <Route exact path="/" element={<LazyHomePage />} />
            </Route>
            <Route path="/login" element={<LazyLoginPage />} />
          </Routes>
        </Suspense>
      </div>
      <ToastContainer />
    </>
  );
}

export default App;
