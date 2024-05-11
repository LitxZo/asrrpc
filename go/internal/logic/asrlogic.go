package logic

import (
	"context"

	"go/go/internal/svc"
	"go/go/pb/asr"

	"github.com/zeromicro/go-zero/core/logx"
)

type ASRLogic struct {
	ctx    context.Context
	svcCtx *svc.ServiceContext
	logx.Logger
}

func NewASRLogic(ctx context.Context, svcCtx *svc.ServiceContext) *ASRLogic {
	return &ASRLogic{
		ctx:    ctx,
		svcCtx: svcCtx,
		Logger: logx.WithContext(ctx),
	}
}

func (l *ASRLogic) ASR(in *asr.AsrRequest) (*asr.AsrResponse, error) {
	// todo: add your logic here and delete this line

	return &asr.AsrResponse{}, nil
}
