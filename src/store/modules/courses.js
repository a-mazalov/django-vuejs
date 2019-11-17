import courseService from '../../services/courseService'

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
	}
}

const mutations = {
	setCourses(state, courses) {
		state.courses = courses
	},
	addCourse(state, course) {
		state.courses.push(course)
	},
	deleteCourse(state, msgId) {
		state.courses = state.courses.filter(obj => obj.pk !== msgId)
	}
}

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
}