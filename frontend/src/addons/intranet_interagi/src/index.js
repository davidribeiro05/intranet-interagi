// Blocos
import MeteoEdit from './components/Blocks/Meteo/Edit';
import MeteoView from './components/Blocks/Meteo/View';
import RespostaView from './components/Blocks/Resposta/View';

// Views
import AreaView from './components/View/AreaView';
import PessoaView from './components/View/PessoaView';

// Icones
import exclamationSVG from '@plone/volto/icons/exclamation.svg';
import meteoSVG from '@plone/volto/icons/cloud.svg';

// reducers
import { meteoData } from './reducers/meteoData';

const applyConfig = (config) => {
  config.settings = {
    ...config.settings,
    isMultilingual: false,
    supportedLanguages: ['pt-br'],
    defaultLanguage: 'pt-br',
  };
  config.blocks.blocksConfig.codeBlock.defaultStyle = 'light';
  config.views.contentTypesViews = {
    ...config.views.contentTypesViews,
    Area: AreaView,
    Pessoa: PessoaView,
  };

  // Blocos
  config.blocks.blocksConfig.respostaBlock = {
    id: 'respostaBlock',
    title: 'Resposta',
    group: 'intranet',
    icon: exclamationSVG,
    view: RespostaView,
    restricted: false,
    mostUsed: false,
    sidebarTab: false,
    blockHasOwnFocusManagement: false,
  };

  config.blocks.blocksConfig.meteoBlock = {
    id: 'meteoBlock',
    title: 'Clima',
    group: 'intranet',
    icon: meteoSVG,
    view: MeteoView,
    edit: MeteoEdit,
    restricted: false,
    mostUsed: false,
    sidebarTab: true,
    blockHasOwnFocusManagement: false,
  };
  // Grupo de Blocos
  config.blocks.groupBlocksOrder = [
    ...config.blocks.groupBlocksOrder,
    { id: 'intranet', title: 'Intranet' },
  ];

  // Reducers
  config.addonReducers = {
    ...config.addonReducers,
    meteoData,
  };

  return config;
};

export default applyConfig;
