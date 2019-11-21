import api from '@/services/api'

export default {
	fetchCourses() {
		return api.get(`courses/`)
			.then(response => response.data)
	},
	postCourse(payload) {
		return api.post(`courses/`, payload)
			.then(response => response.data)
	},
	deleteCourse(msgId) {
		return api.delete(`courses/${msgId}`)
			.then(response => response.data)
	},
	joinCourse(crsId, payload) {
		return api.put(`courses/${crsId}/`, payload)
			.then(response => response.data)
	}
	// joinCourse(crsId) {
	// 	return api.put(`courses/${crsId}`)
	// 		.then(response => response.data)
	// }
}