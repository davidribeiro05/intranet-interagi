import { GET_METEO_DATA } from '../../constants/ActionTypes';

export function getMeteoData() {
  const path = '/@meteo';
  return {
    type: GET_METEO_DATA,
    request: {
      op: 'get',
      path: path,
    },
  };
}
