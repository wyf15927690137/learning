// npm install --save vue-router
// import { createRouter, createWebHashHistory} from "vue-router"
import { createRouter, createWebHistory} from "vue-router"
import HomeView from "../views/HomeView.vue";
// import AboutView from "../views/AboutView.vue";

const routes = [
    {
        path: "/",
        name: "home",
        component:HomeView
    },
    {
        path: "/about",
        name: "about",
        redirect: "/about/info",
        component: () => import("../views/AboutView.vue"),
        children: [
            {
                path: "us",
                component: () => import("../views/About/AboutUs.vue")
            },
            {
                path: "info",
                component: () => import("../views/About/AboutInfo.vue")
            }
        ]
    },
    {
        path: "/news",
        name: "news",
        component: () => import("../views/NewsView.vue")
    },
    {
        path: "/newsdetails/:name",
        name: "details",
        component: () =>import("../views/NewsDetails.vue")
    }
]
const router = createRouter({
        // don't need backend to redirect
        // history: createWebHashHistory(),
        history: createWebHistory(),
        routes
    }
)

export default router;