import courseService from '../../services/courseService'
import store from '@/store'
const state = {
	courses: []
}

const getters = {
	courses: state => {
		return state.courses
	}
}

const actions = {
	getCourses({
		commit
	}) {
		courseService.fetchCourses()
			.then(courses => {





				commit('setCourses', courses)
			})
	},
	addCourse({
		commit
	}, course) {
		courseService.postCourse(course)
			.then(() => {
				commit('addCourse', course)
			})
	},
	deleteCourse({
		commit
	}, msgId) {
		courseService.deleteCourse(msgId)
		commit('deleteCourse', msgId)
	},
	joinCourse({
		commit
	}, crsId) {
		courseService.joinCourse(crsId)
		commit('joinCourse', crsId)
	},
	outCourse({
		commit
	}, crsId) {
		courseService.outCourse(crsId)
		commit('outCourse', crsId)
	}
}

const mutations = {
	setCourses(state, courses) {

		// console.log('STORE CR', this.$store.state.auth.userInfo.courses);
		console.log('STORE CR', store.getters['auth/userInfo'].courses);

		if (store.getters['auth/userInfo'].courses) {
			for (let user_in_course of store.getters['auth/userInfo'].courses) {
				for (let item of courses) {
					console.log(item.id, user_in_course);
					if (item.id == user_in_course) {
						item.isFollow = true;
					}
				}
			}
		}




		state.courses = courses
	},
	addCourse(state, course) {
		state.courses.push(course)
	},
	deleteCourse(state, msgId) {
		state.courses = state.courses.filter(obj => obj.pk !== msgId)
	},
	joinCourse(state, crsId) {
		console.log(state, crsId);
		// state.courses = state.course.map(obj => obj.pk !== crsId)
	},
	outCourse(state, crsId) {
		console.log(state, crsId);
		// state.courses = state.course.map(obj => obj.pk !== crsId)
	}
}

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
}