#!/system/sh

rm /sdcard/info.txt
touch /sdcard/info.txt
cd /sdcard

cscofi=$(getprop ril.official_cscver)
echo $cscofi >> info.txt
serianum=$(getprop ril.serialnumber)
echo $serianum >> info.txt
libargc=$(getprop rild.libargs)
echo $libargc >> info.txt
sacode=$(getprop ril.sales_code)
echo $sacode >> info.txt
hw=$(getprop ril.hw_ver)
echo $hw >> info.txt
boardmodem=$(getprop ril.modem.board)
echo $boardmodem >> info.txt
rilinfo=$(getprop gsm.version.ril-impl)
echo $rilinfo >> info.txt
languagedef=$(getprop persist.sys.language)
echo $languagedef >> info.txt
timezone=$(getprop persist.sys.timezone)
echo $timezone >> info.txt
serialno=$(getprop ro.boot.serialno)
echo $serialno >> info.txt
pda=$(getprop ro.build.PDA)
echo $pda >> info.txt
osversion=$(getprop ro.build.version.release)
echo $osversion >> info.txt
sdkversion=$(getprop ro.build.version.sdk)
echo $sdkversion >> info.txt
clientos=$(getprop ro.com.google.clientidbase)
echo $clientos >> info.txt
countrycode=$(getprop ro.csc.country_code)
echo $countrycode >> info.txt
model=$(getprop ro.product.model)
echo $model >> info.txt