import React, { lazy, Suspense, useEffect } from "react";
import PrivateRoute from "./router/PrivateRoute";
import { useSelector, useDispatch } from "react-redux";
import { Routes, Route, BrowserRouter, Navigate } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
// import {
//   dispatchLogin,
//   fetchUser,
//   dispatchGetUser,
// } from "./redux/actions/authAction";

// import AccountServices from "./services/AccountServices";
import Loading from "./components/Loading/Loading";

const LazyLoginPage = lazy(() => import("./views/LoginPage/LoginPage"));
const LazyHomePage = lazy(() => import("./views/HomePage/HomePage"));
// const LazyAccountPage = lazy(() => import("./components/"));

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
