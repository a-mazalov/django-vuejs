import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from 'vuex/dist/logger';

import auth from './auth';
import password from './password';
import signup from './signup';
import messages from './modules/messages'
import courses from './modules/courses'

// const debug = process.env.NODE_ENV !== 'production';
const debug = true;

Vue.use(Vuex);

export default new Vuex.Store({
	modules: {
		auth,
		password,
		signup,
		messages,
		courses,
	},
	strict: debug,
	plugins: debug ? [createLogger()] : [],
})