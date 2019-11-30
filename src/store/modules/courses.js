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
				console.log(courses);
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
	}, crsId, data) {
		courseService.joinCourse(crsId, data)
		commit('joinCourse', crsId, data)
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
	},
	joinCourse(state, crsId) {
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