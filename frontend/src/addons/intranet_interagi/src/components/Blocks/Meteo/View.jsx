import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getMeteoData } from '../../../actions/Meteo/Meteo';

const MeteoView = (props) => {
  const { data } = props;
  // Pointer para o local com os dados
  const previsao = useSelector((state) => state.meteoData?.data || {});
  const sunrise = previsao?.sunrise ? previsao.sunrise[0] : '';
  const sunset = previsao?.sunset ? previsao.sunset[0] : '';
  const measure = data?.measure ? data.measure : '';
  const dispatch = useDispatch();

  // Busca os dados
  useEffect(() => {
    dispatch(getMeteoData());
  }, [dispatch, data]);

  return (
    <div className={'block blockMeteo'}>
      <div className={'container'}>
        <header>{data.header ? data.header : 'Sem Título'}</header>
        <main>
          {measure === 'sunset' && (
            <>
              <span>Por do sol</span>: <span>{sunset}</span>
            </>
          )}
          {measure === 'sunrise' && (
            <>
              <span>Nascer do Sol</span>: <span>{sunrise}</span>
            </>
          )}
        </main>
      </div>
    </div>
  );
};

export default MeteoView;
