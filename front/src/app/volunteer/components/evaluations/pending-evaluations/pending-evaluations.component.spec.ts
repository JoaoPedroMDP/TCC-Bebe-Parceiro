import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PendingEvaluationsComponent } from './pending-evaluations.component';

describe('PendingEvaluationsComponent', () => {
  let component: PendingEvaluationsComponent;
  let fixture: ComponentFixture<PendingEvaluationsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PendingEvaluationsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PendingEvaluationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
