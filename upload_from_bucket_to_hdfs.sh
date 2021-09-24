usage() {
  echo -e "Usage: $0 [-f <format>] [-o <hdfs path>]\n"\
       "where\n"\
       "-b defines an cloud bucket path\n"\
       "-d defines an hdfs destination path\n"\
       "\n"\
        1>&2
  exit 1
}

while getopts ":f:d:" opt; do
    case "$opt" in
        b)  BUCKET_PATH=${OPTARG} ;;
        d)  HDFS_PATH=${OPTARG} ;;
        *)  usage ;;
    esac
done

if [[ -z "$HDFS_PATH" ]];
then
  HDFS_PATH="/bdpc/hadoop_mr/2015_Flight_Delays_and_Cancellations/input"
  hadoop fs -rm -R "$HDFS_PATH"
  hdfs dfs -mkdir -p "$HDFS_PATH"
fi

if [[ -z "$BUCKET_PATH" ]];
then
  BUCKET_PATH="gs://gl-procamp-bigdata-datasets/2015_Flight_Delays_and_Cancellations/flights.csv"
fi

echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
echo "BUCKET_PATH = $BUCKET_PATH"
echo "HDFS_PATH = $HDFS_PATH"
echo "-------------------------------------"


SUBMIT_CMD="hadoop distcp ${BUCKET_PATH} ${HDFS_PATH}"
echo "$SUBMIT_CMD"
${SUBMIT_CMD}

echo "<<<<<<<<<<<<<<<<<<  HDFS  <<<<<<<<<<<<<<<<<<<<<"

hdfs dfs -ls ${HDFS_PATH}

echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"